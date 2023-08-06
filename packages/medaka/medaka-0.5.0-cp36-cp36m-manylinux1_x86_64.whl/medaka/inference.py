from collections import Counter, deque
from concurrent.futures import ProcessPoolExecutor, Future
import functools
import inspect
import itertools
import logging
from math import ceil
import os
import queue
import threading
import time
from timeit import default_timer as now

import numpy as np
import pysam

from medaka import vcf
from medaka.datastore import DataStore, DataIndex
from medaka.common import (get_regions, decoding, grouper, mkdir_p, Sample,
                           _gap_, threadsafe_generator, get_named_logger)

from medaka.features import SampleGenerator
import medaka.models


def weighted_categorical_crossentropy(weights):
    """
    A weighted version of keras.objectives.categorical_crossentropy
    @url: https://gist.github.com/wassname/ce364fddfc8a025bfab4348cf5de852d
    @author: wassname

    Variables:
        weights: numpy array of shape (C,) where C is the number of classes

    Usage:
        weights = np.array([0.5,2,10]) # Class one at 0.5, class 2 twice the normal weights, class 3 10x.
        loss = weighted_categorical_crossentropy(weights)
        model.compile(loss=loss,optimizer='adam')
    """
    from keras import backend as K
    weights = K.variable(weights)

    def loss(y_true, y_pred):
        # scale predictions so that the class probas of each sample sum to 1
        y_pred /= K.sum(y_pred, axis=-1, keepdims=True)
        # clip to prevent NaN's and Inf's
        y_pred = K.clip(y_pred, K.epsilon(), 1 - K.epsilon())
        # calc
        loss = y_true * K.log(y_pred) * weights
        loss = -K.sum(loss, -1)
        return loss

    return loss


def qscore(y_true, y_pred):
    from keras import backend as K
    error = K.cast(K.not_equal(
        K.max(y_true, axis=-1), K.cast(K.argmax(y_pred, axis=-1), K.floatx())),
        K.floatx()
    )
    error = K.sum(error) / K.sum(K.ones_like(error))
    return -10.0 * 0.434294481 * K.log(error)


def run_training(train_name, batcher, model_fp=None,
                 epochs=5000, class_weight=None, n_mini_epochs=1):
    """Run training."""
    from keras.callbacks import ModelCheckpoint, CSVLogger, TensorBoard, EarlyStopping

    logger = get_named_logger('RunTraining')

    if model_fp is None:
        model_name = medaka.models.default_model
        model_kwargs = {
            k:v.default for (k,v) in
            inspect.signature(medaka.models.model_builders[model_name]).parameters.items()
            if v.default is not inspect.Parameter.empty
        }
    else:
        with DataStore(model_fp) as ds:
            model_name = ds.meta['medaka_model_name']
            model_kwargs = ds.meta['medaka_model_kwargs']

    opt_str = '\n'.join(['{}: {}'.format(k,v) for k, v in model_kwargs.items()])
    logger.info('Building {} model with: \n{}'.format(model_name, opt_str))
    num_classes = len(batcher.label_counts)
    timesteps, feat_dim = batcher.feature_shape
    model = medaka.models.model_builders[model_name](timesteps, feat_dim, num_classes, **model_kwargs)

    if model_fp is not None:
        try:
            model.load_weights(model_fp)
            logger.info("Loading weights from {}".format(model_fp))
        except:
            logger.info("Could not load weights from {}".format(model_fp))

    msg = "feat_dim: {}, timesteps: {}, num_classes: {}"
    logger.info(msg.format(feat_dim, timesteps, num_classes))
    model.summary()

    model_details = batcher.meta.copy()

    model_details['medaka_model_name'] = model_name
    model_details['medaka_model_kwargs'] = model_kwargs
    model_details['medaka_label_decoding'] = batcher.label_decoding

    opts = dict(verbose=1, save_best_only=True, mode='max')

    # define class here to avoid top-level keras import
    class ModelMetaCheckpoint(ModelCheckpoint):
        """Custom ModelCheckpoint to add medaka-specific metadata to model files"""
        def __init__(self, medaka_meta, *args, **kwargs):
            super(ModelMetaCheckpoint, self).__init__(*args, **kwargs)
            self.medaka_meta = medaka_meta

        def on_epoch_end(self, epoch, logs=None):
            super(ModelMetaCheckpoint, self).on_epoch_end(epoch, logs)
            filepath = self.filepath.format(epoch=epoch + 1, **logs)
            with DataStore(filepath, 'a') as ds:
                ds.meta.update(self.medaka_meta)

    callbacks = [
        # Best model according to training set accuracy
        ModelMetaCheckpoint(model_details, os.path.join(train_name, 'model.best.hdf5'),
                            monitor='acc', **opts),
        # Best model according to validation set accuracy
        ModelMetaCheckpoint(model_details, os.path.join(train_name, 'model.best.val.hdf5'),
                        monitor='val_acc', **opts),
        # Best model according to validation set qscore
        ModelMetaCheckpoint(model_details, os.path.join(train_name, 'model.best.val.qscore.hdf5'),
                        monitor='val_qscore', **opts),
        # Checkpoints when training set accuracy improves
        ModelMetaCheckpoint(model_details, os.path.join(train_name, 'model-acc-improvement-{epoch:02d}-{acc:.2f}.hdf5'),
                        monitor='acc', **opts),
        ModelMetaCheckpoint(model_details, os.path.join(train_name, 'model-val_acc-improvement-{epoch:02d}-{val_acc:.2f}.hdf5'),
                        monitor='val_acc', **opts),
        # Stop when no improvement, patience is number of epochs to allow no improvement
        EarlyStopping(monitor='val_loss', patience=20),
        # Log of epoch stats
        CSVLogger(os.path.join(train_name, 'training.log')),
        # Allow us to run tensorboard to see how things are going. Some
        #   features require validation data, not clear why.
        #TensorBoard(log_dir=os.path.join(train_name, 'logs'),
        #            histogram_freq=5, batch_size=100, write_graph=True,
        #            write_grads=True, write_images=True)
    ]

    if class_weight is not None:
        loss = weighted_categorical_crossentropy(class_weight)
        logger.info("Using weighted_categorical_crossentropy loss function")
    else:
        loss = 'sparse_categorical_crossentropy'
        logger.info("Using {} loss function".format(loss))

    model.compile(
       loss=loss,
       optimizer='rmsprop',
       metrics=['accuracy', qscore],
    )

    if n_mini_epochs == 1:
        logging.info("Not using mini_epochs, an epoch is a full traversal of the training data")
    else:
        logging.info("Using mini_epochs, an epoch is a traversal of 1/{} of the training data".format(n_mini_epochs))

    # fit generator
    model.fit_generator(
        batcher.gen_train(), steps_per_epoch=ceil(batcher.n_train_batches/n_mini_epochs),
        validation_data=batcher.gen_valid(), validation_steps=batcher.n_valid_batches,
        max_queue_size=8, workers=1, use_multiprocessing=False,
        epochs=epochs,
        #verbose=False,
        callbacks=callbacks,
        class_weight=class_weight,
    )


class TrainBatcher():
    def __init__(self, features, max_label_len, validation=0.2, seed=0, sparse_labels=True, batch_size=500, threads=1):
        """
        Class to server up batches of training / validation data.

        :param features: iterable of str, training feature files.
        :param max_label_len: int, maximum label length, longer labels will be truncated.
        :param validation: float, fraction of batches to use for validation, or
                iterable of str, validation feature files.
        :param seed: int, random seed for separation of batches into training/validation.
        :param sparse_labels: bool, create sparse labels.
        """
        self.logger = get_named_logger('TrainBatcher')

        self.features = features
        self.max_label_len = max_label_len
        self.validation = validation
        self.seed = seed
        self.sparse_labels = sparse_labels
        self.batch_size = batch_size

        di = DataIndex(self.features, threads=threads)
        self.samples = di.samples.copy()
        self.meta = di.meta.copy()
        self.label_counts = self.meta['medaka_label_counts']

        # check sample size using first batch
        test_sample, test_fname = self.samples[0]
        with DataStore(test_fname) as ds:
            self.feature_shape = ds.load_sample(test_sample).features.shape
        self.logger.info("Sample features have shape {}".format(self.feature_shape))

        if isinstance(self.validation, float):
            np.random.seed(self.seed)
            np.random.shuffle(self.samples)
            n_sample_train = int((1 - self.validation) * len(self.samples))
            self.train_samples = self.samples[:n_sample_train]
            self.valid_samples = self.samples[n_sample_train:]
            msg = 'Randomly selected {} ({:3.2%}) of features for validation (seed {})'
            self.logger.info(msg.format(len(self.valid_samples), self.validation, self.seed))
        else:
            self.train_samples = self.samples
            self.valid_samples = DataIndex(self.validation).samples.copy()
            msg = 'Found {} validation samples equivalent to {:3.2%} of all the data'
            fraction = len(self.valid_samples) / len(self.valid_samples) + len(self.train_samples)
            self.logger.info(msg.format(len(self.valid_samples), fraction))

        self.n_train_batches = ceil(len(self.train_samples) / batch_size)
        self.n_valid_batches = ceil(len(self.valid_samples) / batch_size)

        msg = 'Got {} samples in {} batches ({} labels) for {}'
        self.logger.info(msg.format(len(self.train_samples),
                                    self.n_train_batches,
                                    len(self.train_samples) * self.feature_shape[0],
                                    'training'))
        self.logger.info(msg.format(len(self.valid_samples),
                                    self.n_valid_batches,
                                    len(self.valid_samples) * self.feature_shape[0],
                                    'validation'))

        self.n_classes = len(self.label_counts)

        # get label encoding, given max_label_len
        self.logger.info("Max label length: {}".format(self.max_label_len if self.max_label_len is not None else 'inf'))
        self.label_encoding, self.label_decoding, self.label_counts = process_labels(self.label_counts, max_label_len=self.max_label_len)

        prep_func = functools.partial(TrainBatcher.sample_to_x_y,
                                      max_label_len=self.max_label_len,
                                      label_encoding=self.label_encoding,
                                      sparse_labels=self.sparse_labels,
                                      n_classes=self.n_classes)

        self.threads = threads
        self.executor = ProcessPoolExecutor(self.threads)
        self._valid_queue = BatchQueue(self.valid_samples, prep_func,
                                       self.batch_size, self.executor,
                                       self.seed, name='ValidBatcher',
                                       maxsize=min(2 * self.n_valid_batches,
                                                   100),)
        self._train_queue = BatchQueue(self.train_samples, prep_func,
                                       self.batch_size, self.executor,
                                       self.seed, name='TrainBatcher',
                                       maxsize=min(2 * self.n_train_batches,
                                                   100),)


    @staticmethod
    def sample_to_x_y(sample, max_label_len, label_encoding, sparse_labels, n_classes):
        """Convert a `Sample` object into an x,y tuple for training.

        :param sample: (filename, sample key)
        :param max_label_len: int, maximum label length, longer labels will be truncated.
        :param label_encoding: {label: int encoded label}.
        :param sparse_labels: bool, create sparse labels.
        :param n_classes: int, number of label classes.
        :returns: (np.ndarray of inputs, np.ndarray of labels)
        """
        sample_key, sample_file = sample

        with DataStore(sample_file) as ds:
            s = ds.load_sample(sample_key)
        if s.labels is None:
            raise ValueError("Cannot train without labels.")
        x = s.features
        # labels can either be unicode strings or (base, length) integer tuples
        if isinstance(s.labels[0], np.unicode):
            # TODO: is this ever used now we have dispensed with tview code?
            y = np.fromiter((label_encoding[l[:min(max_label_len, len(l))]]
                               for l in s.labels), dtype=int, count=len(s.labels))
        else:
            y = np.fromiter((label_encoding[tuple((l['base'], min(max_label_len, l['run_length'])))]
                             for l in s.labels), dtype=int, count=len(s.labels))
        y = y.reshape(y.shape + (1,))
        if not sparse_labels:
            from keras.utils.np_utils import to_categorical
            y = to_categorical(y, num_classes=n_classes)
        return x, y


    @staticmethod
    def samples_to_batch(samples, prep_func, name, batch, epoch):
        t0 = now()
        items = [prep_func(s) for s in samples]
        xs, ys = zip(*items)
        x, y = np.stack(xs), np.stack(ys)
        get_named_logger(name).debug("Took {:5.3}s to load batch {} (epoch {})".format(now()-t0, batch, epoch))
        return x, y


    def stop(self):
        self._train_queue.stop()
        self._valid_queue.stop()


    @threadsafe_generator
    def gen_train(self):
        yield from self._train_queue.yield_batches()


    @threadsafe_generator
    def gen_valid(self):
        yield from self._valid_queue.yield_batches()


class BatchQueue(object):
    def  __init__(self, samples, prep_func, batch_size, executor, seed=None, name='Batcher', maxsize=100):
        """Load and queue training samples into batches from `.hdf` files.

        :param samples: tuples of (filename, hdf sample key).
        :param prep_func: function to transform a sample to x,y data.
        :param batch_size: group samples by this number.
        :param executor: `ThreadPoolExecutor` instance.
        :param seed: seed for shuffling.
        :param name: str, name for logger.
        :param maxsize: int, maximum queue size.

        Once initialized batches can be retrieved using batch_q._queue.get().

        """
        self.samples = samples
        self.prep_func = prep_func
        self.batch_size = batch_size

        if seed is not None:
            np.random.seed(seed)

        self.name = name
        self.logger = get_named_logger(name)
        self.maxsize = maxsize
        self._queue = queue.Queue(maxsize=self.maxsize)
        self._queue = queue.Queue(maxsize=self.maxsize)
        self.executor = executor
        self.stopped = threading.Event()
        self.qthread = threading.Thread(target=self._fill_queue_batch)
        self.qthread.start()
        time.sleep(2)
        self.logger.info("Started reading samples from files with queue size {}".format(maxsize))


    def stop(self, timeout=5):
        self.logger.info("About to stop.")
        self.stopped.set()
        self.logger.info("Waiting for read thread.")
        self.qthread.join(timeout)
        if self.qthread.is_alive:
            self.logger.critical("Read thread did not terminate after {}s.".format(timeout))


    def _fill_queue_batch(self):
        epoch = 0
        self.loaded_batches = 0
        self.submitted_batches = 0
        self.taken_batches = 0
        while not self.stopped.is_set():
            batch = 0
            np.random.shuffle(self.samples)
            for samples in grouper(iter(self.samples), batch_size=self.batch_size):
                if self.stopped.is_set(): # the loop is potentially long-running
                    self.logger.info("Batching stopped.")
                    return
                res = self.executor.submit(TrainBatcher.samples_to_batch, samples, self.prep_func, self.name, batch, epoch)
                res.add_done_callback(self._count_finished)
                while True: # keep an eye on the stopped flag
                    try:
                        self._queue.put(res, timeout=1)
                    except queue.Full:
                        #self.logger.debug("Queue is full ({}), cannot put, trying again.".format(self._queue.qsize()))
                        if self.stopped.is_set():
                            self.logger.info("Batching stopped.")
                            return
                    else:
                        #self.logger.debug("Successfully put sample (future).")
                        self.submitted_batches += 1
                        break
                batch += 1
            epoch += 1
        self.logger.info("Batching stopped.")
        return

    def _count_finished(self, future):
        self.loaded_batches += 1


    @threadsafe_generator
    def yield_batches(self):
        time_between = deque(maxlen=50)
        get_time = deque(maxlen=50)
        t0 = now()
        try:
            while True:
                t0, t1 = now(), t0
                ta = now()
                res = self._queue.get()
                if isinstance(res, Future):
                    res =  res.result()
                get_time.append(now() - ta)
                time_between.append(t0 - t1)
                get_rate = np.mean(get_time)
                req_rate = np.mean(time_between) - get_rate
                self.logger.debug(
                    "Request every: {:5.3}s. Fetch time: {:5.3}.".format(
                    np.mean(time_between), np.mean(get_time)
                ))
                self.logger.debug("Queue state: {}/{} ready.".format(
                    self.loaded_batches - self.taken_batches,
                    self.submitted_batches - self.taken_batches
                ))
                self.taken_batches += 1
                yield res
        except Exception as e:
            self.logger.critical("Exception caught why yielding batches: {}".format(e))
            self.stop()
            raise e


class VarQueue(list):

    @property
    def last_pos(self):
        if len(self) == 0:
            return None
        else:
            return self[-1].pos

    def write(self, vcf_fh):
        if len(self) > 1:
            are_dels = all(len(x.ref) == 2 for x in self)
            are_same_ref = len(set(x.chrom for x in self)) == 1
            if are_dels and are_same_ref:
                name = self[0].chrom
                pos = self[0].pos
                ref = ''.join((x.ref[0] for x in self))
                ref += self[-1].ref[-1]
                alt = ref[0]

                merged_var = vcf.Variant(name, pos, ref, alt, info=info)
                vcf_fh.write_variant(merged_var)
            else:
                raise ValueError('Cannot merge variants: {}.'.format(self))
        elif len(self) == 1:
            vcf_fh.write_variant(self[0])
        del self[:]


class VCFChunkWriter(object):
    def __init__(self, fname, chrom, start, end, reference_fasta, label_decoding):
        vcf_region_str = '{}:{}-{}'.format(chrom, start, end) #is this correct?
        self.label_decoding = label_decoding
        self.logger = get_named_logger('VCFWriter')
        self.logger.info("Writing variants for {}".format(vcf_region_str))

        vcf_meta = ['region={}'.format(vcf_region_str)]
        self.writer = vcf.VCFWriter(fname, meta_info=vcf_meta)
        self.ref_fasta = pysam.FastaFile(reference_fasta)

    def __enter__(self):
        self.writer.__enter__()
        self.ref_fasta.__enter__()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.writer.__exit__(exc_type, exc_val, exc_tb)
        self.ref_fasta.__exit__(exc_type, exc_val, exc_tb)

    def add_chunk(self, sample, pred):
        # Write consensus alts to vcf
        cursor = 0
        var_queue = list()
        ref_seq = self.ref_fasta.fetch(sample.ref_name)
        for pos, grp in itertools.groupby(sample.positions['major']):
            end = cursor + len(list(grp))
            alt = ''.join(self.label_decoding[x] for x in pred[cursor:end]).replace(_gap_, '')
            # For simple insertions and deletions in which either
            #   the REF or one of the ALT alleles would otherwise be
            #   null/empty, the REF and ALT Strings must include the
            #   base before the event (which must be reflected in
            #   the POS field), unless the event occurs at position
            #   1 on the contig in which case it must include the
            #   base after the event
            if alt == '':
                # deletion
                if pos == 0:
                    # the "unless case"
                    ref = ref_seq[1]
                    alt = ref_seq[1]
                else:
                    # the usual case
                    pos = pos - 1
                    ref = ref_seq[pos:pos+2]
                    alt = ref_seq[pos]
            else:
                ref = ref_seq[pos]

            # Merging of variants produced by considering major.{minor} positions
            # These are of the form:
            #    X -> Y          - subs
            #    prev.X -> prev  - deletion
            #    X -> Xyy..      - insertion
            # In the second case we may need to merge variants from consecutive
            # major positions.
            if alt == ref:
                self.write(var_queue)
                var_queue = list()
            else:
                var = vcf.Variant(sample.ref_name, pos, ref, alt)
                if len(var_queue) == 0 or pos - var_queue[-1].pos == 1:
                    var_queue.append(var)
                else:
                    self.write(var_queue)
                    var_queue = [var]
            cursor = end
        self.write(var_queue)


    def write(self, var_queue):
        if len(var_queue) > 1:
            are_dels = all(len(x.ref) == 2 for x in var_queue)
            are_same_ref = len(set(x.chrom for x in var_queue)) == 1
            if are_dels and are_same_ref:
                name = var_queue[0].chrom
                pos = var_queue[0].pos
                ref = ''.join((x.ref[0] for x in var_queue))
                ref += var_queue[-1].ref[-1]
                alt = ref[0]

                merged_var = vcf.Variant(name, pos, ref, alt)
                self.writer.write_variant(merged_var)
            else:
                raise ValueError('Cannot merge variants: {}.'.format(var_queue))
        elif len(var_queue) == 1:
            self.writer.write_variant(var_queue[0])


def run_prediction(output, bam, regions, model, model_file, rle_ref, read_fraction, chunk_len, chunk_ovlp,
                   batch_size=200):
    """Inference worker."""

    logger = get_named_logger('PWorker')

    def sample_gen():
        # chain all samples whilst dispensing with generators when done
        #   (they hold the feature vector in memory until they die)
        for region in regions:
            data_gen = SampleGenerator(
                bam, region, model_file, rle_ref, read_fraction,
                chunk_len=chunk_len, chunk_overlap=chunk_ovlp)
            yield from data_gen.samples
    batches = grouper(sample_gen(), batch_size)

    total_region_mbases = sum(r.size for r in regions) / 1e6
    logger.info("Running inference for {:.1f}M draft bases.".format(total_region_mbases))

    with DataStore(output, 'a') as ds:
        mbases_done = 0

        t0 = now()
        tlast = t0
        for data in batches:
            x_data = np.stack([x.features for x in data])
            # TODO: change to predict_on_batch?
            class_probs = model.predict(x_data, batch_size=batch_size, verbose=0)
            mbases_done += sum(x.span for x in data) / 1e6
            mbases_done = min(mbases_done, total_region_mbases)  # just to avoid funny log msg
            t1 = now()
            if t1 - tlast > 10:
                tlast = t1
                msg = '{:.1%} Done ({:.1f}/{:.1f} Mbases) in {:.1f}s'
                logger.info(msg.format(mbases_done / total_region_mbases, mbases_done, total_region_mbases, t1 - t0))

            best = np.argmax(class_probs, -1)
            for sample, prob, pred in zip(data, class_probs, best):
                # write out positions and predictions for later analysis
                sample_d = sample._asdict()
                sample_d['label_probs'] = prob
                sample_d['features'] = None  # to keep file sizes down
                ds.write_sample(Sample(**sample_d))

    logger.info('All done')
    return None


def predict(args):
    """Inference program."""
    os.environ["TF_CPP_MIN_LOG_LEVEL"]="2"
    from keras.models import load_model
    from keras import backend as K

    args.regions = get_regions(args.bam, region_strs=args.regions)
    logger = get_named_logger('Predict')
    logger.info('Processing region(s): {}'.format(' '.join(str(r) for r in args.regions)))

    # write class names to output
    with DataStore(args.model) as ds:
        meta = ds.meta
    with DataStore(args.output, 'w') as ds:
        ds.update_meta(meta)

    logger.info("Setting tensorflow threads to {}.".format(args.threads))
    K.tf.logging.set_verbosity(K.tf.logging.ERROR)
    K.set_session(K.tf.Session(
        config=K.tf.ConfigProto(
            intra_op_parallelism_threads=args.threads,
            inter_op_parallelism_threads=args.threads)
    ))

    # Split overly long regions to maximum size so as to not create
    #   massive feature matrices, then segregate those which cannot be
    #   batched.
    MAX_REGION_SIZE = int(1e6)  # 1Mb
    long_regions = []
    short_regions = []
    for region in args.regions:
        if region.size > MAX_REGION_SIZE:
            regs = region.split(MAX_REGION_SIZE, args.chunk_ovlp)
        else:
            regs = [region]
        for r in regs:
            if r.size > args.chunk_len:
                long_regions.append(r)
            else:
                short_regions.append(r)
    logger.info("Found {} long and {} short regions.".format(
        len(long_regions), len(short_regions)))

    if len(long_regions) > 0:
        logger.info("Processing long regions.")
        model = medaka.models.load_model(args.model, time_steps=args.chunk_len)
        run_prediction(
            args.output, args.bam, long_regions, model, args.model, args.rle_ref, args.read_fraction,
            args.chunk_len, args.chunk_ovlp,
            batch_size=args.batch_size
        )

    # short regions must be done individually since they have differing lengths
    #   TODO: consider masking (it appears slow to apply wholesale), maybe
    #         step down args.chunk_len by a constant factor until nothing remains.
    if len(short_regions) > 0:
        logger.info("Processing short regions")
        model = medaka.models.load_model(args.model, time_steps=None)
        for region in short_regions:
            chunk_len = region.size // 2
            chunk_ovlp = chunk_len // 10 # still need overlap as features will be longer
            run_prediction(
                args.output, args.bam, [region], model, args.model, args.rle_ref, args.read_fraction,
                chunk_len, chunk_ovlp,
                batch_size=args.batch_size
            )
    logger.info("Finished processing all regions.")


def process_labels(label_counts, max_label_len=10):
    """Create map from full labels to (encoded) truncated labels.

    :param label_counrs: `Counter` obj of label counts.
    :param max_label_len: int, maximum label length, longer labels will be truncated.
    :returns:
    :param label_encoding: {label: int encoded label}.
    :param sparse_labels: bool, create sparse labels.
    :param n_classes: int, number of label classes.
    :returns: ({label: int encoding}, [label decodings], `Counter` of truncated counts).
    """
    logger = get_named_logger('Labelling')

    old_labels = [k for k in label_counts.keys()]
    if type(old_labels[0]) == tuple:
        new_labels = (l[1] * decoding[l[0]].upper() for l in old_labels)
    else:
        new_labels = [l for l in old_labels]

    if max_label_len < np.inf:
        new_labels = [l[:max_label_len] for l in new_labels]

    old_to_new = dict(zip(old_labels, new_labels))
    label_decoding = list(sorted(set(new_labels)))
    label_encoding = { l: label_decoding.index(old_to_new[l]) for l in old_labels}
    logger.info("Label encoding dict is:\n{}".format('\n'.join(
        '{}: {}'.format(k, v) for k, v in label_encoding.items()
    )))

    new_counts = Counter()
    for l in old_labels:
        new_counts[label_encoding[l]] += label_counts[l]
    logger.info("New label counts {}".format(new_counts))

    return label_encoding, label_decoding, new_counts


def train(args):
    """Training program."""
    train_name = args.train_name
    mkdir_p(train_name, info='Results will be overwritten.')

    logger = get_named_logger('Training')
    logger.debug("Loading datasets:\n{}".format('\n'.join(args.features)))

    sparse_labels = not args.balanced_weights

    args.validation = args.validation_features if args.validation_features is not None else args.validation_split

    batcher = TrainBatcher(args.features, args.max_label_len, args.validation,
                           args.seed, sparse_labels, args.batch_size, threads=args.threads_io)

    if args.balanced_weights:
        n_labels = sum(batcher.label_counts.values())
        n_classes = len(batcher.label_counts)
        class_weight = {k: float(n_labels)/(n_classes * count) for (k, count) in batcher.label_counts.items()}
        class_weight = np.array([class_weight[c] for c in sorted(class_weight.keys())])
    else:
        class_weight = None

    h = lambda d, i: d[i] if d is not None else 1
    logger.info("Label statistics are:\n{}".format('\n'.join(
        '{} ({}) {} (w. {:9.6f})'.format(i, l, batcher.label_counts[i], h(class_weight, i))
            for i, l in enumerate(batcher.label_decoding)
    )))

    # From empirical evidence setting a device here allows code to run 5-6X
    # faster than setting CUDA_VISIBLE_DEVICES environment variable. A small
    # (200Mb) amount of memory will be used on other devices by doing this. The
    # option to set CUDA_VISIBLE_DEVICES is still available (but will renumber
    # the device that should be given on the cmdline).
    import tensorflow as tf
    with tf.device('/gpu:{}'.format(args.device)):
        run_training(
            train_name, batcher, model_fp=args.model, epochs=args.epochs,
            class_weight=class_weight, n_mini_epochs=args.mini_epochs)

    # stop batching threads
    batcher.stop()
    logger.info("Training finished.")
