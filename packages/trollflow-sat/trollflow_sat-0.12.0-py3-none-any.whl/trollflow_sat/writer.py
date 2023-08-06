
import Queue
from threading import Thread
import logging
import time
import os.path

from posttroll.publisher import Publish
from posttroll.message import Message
from trollflow_sat import utils
from trollsift import compose


class DataWriterContainer(object):

    '''Container for DataWriter instance
    '''

    logger = logging.getLogger("DataWriterContainer")
    _prev_lock = None

    def __init__(self, topic=None, port=0, nameservers=None,
                 save_settings=None, use_lock=False):
        self.topic = topic
        self._input_queue = None
        self.output_queue = None  # Queue.Queue()
        self.thread = None
        self.use_lock = use_lock

        if nameservers is None:
            nameservers = []
        else:
            if type(nameservers) not in (list, tuple, set):
                nameservers = [nameservers, ]

        # Create a Writer instance
        self.writer = DataWriter(queue=self.input_queue,
                                 save_settings=save_settings,
                                 topic=topic,
                                 port=port, nameservers=nameservers,
                                 prev_lock=self._prev_lock)
        # Start Writer instance into a new daemonized thread.
        self.thread = Thread(target=self.writer.run)
        self.thread.setDaemon(True)
        self.thread.start()

    @property
    def input_queue(self):
        """Property writer"""
        return self._input_queue

    @input_queue.setter
    def input_queue(self, queue):
        """Set writer queue"""
        self._input_queue = queue
        self.writer.queue = queue

    @property
    def prev_lock(self):
        """Property writer"""
        return self._prev_lock

    @prev_lock.setter
    def prev_lock(self, lock):
        """Set lock of the previous worker"""
        if self.use_lock:
            self._prev_lock = lock
            self.writer.prev_lock = lock

    def __setstate__(self, state):
        self.__init__(**state)

    def restart(self):
        '''Restart writer after configuration update.
        '''
        if self.writer is not None:
            if self.writer.loop:
                self.stop()
        self.__init__()

    def stop(self):
        '''Stop writer.'''
        self.logger.debug("Stopping writer.")
        self.writer.stop()
        self.thread.join()
        self.logger.debug("Writer stopped.")
        self.thread = None

    def is_alive(self):
        """Return the thread status"""
        return self.thread.is_alive()


class DataWriter(Thread):

    """Writes data to disk.
    """

    logger = logging.getLogger("DataWriter")

    def __init__(self, queue=None, save_settings=None,
                 topic=None, port=0, nameservers=None, prev_lock=None):
        Thread.__init__(self)
        self.queue = queue
        self._loop = False
        if save_settings is not None:
            self._save_settings = save_settings
        else:
            self._save_settings = {}
        self._port = port
        if nameservers is None:
            self._nameservers = []
        else:
            if type(nameservers) not in (list, tuple, set):
                nameservers = [nameservers, ]
            self._nameservers = nameservers
        self._topic = topic
        self.prev_lock = prev_lock

    def run(self):
        """Run the thread."""
        self._loop = True
        # Parse settings for saving
        compression = self._save_settings.get('compression', 6)
        tags = self._save_settings.get('tags', None)
        fformat = self._save_settings.get('fformat', None)
        gdal_options = self._save_settings.get('gdal_options', None)
        blocksize = self._save_settings.get('blocksize', None)

        # Initialize publisher context
        with Publish("l2producer", port=self._port,
                     nameservers=self._nameservers) as pub:

            while self._loop:
                if self.queue is not None:
                    try:
                        obj = self.queue.get(True, 1)
                        if self.prev_lock is not None:
                            self.logger.debug("Writer acquires lock of "
                                              "previous worker: %s",
                                              str(self.prev_lock))
                            utils.acquire_lock(self.prev_lock)
                        self.queue.task_done()
                    except Queue.Empty:
                        continue
                    for fname in obj.info["fnames"]:
                        self.logger.info("Saving %s", fname)
                        obj.save(fname, compression=compression, tags=tags,
                                 fformat=fformat, gdal_options=gdal_options,
                                 blocksize=blocksize)

                        area = getattr(obj, "area")
                        try:
                            area_data = {"name": area.name,
                                         "area_id": area.area_id,
                                         "proj_id": area.proj_id,
                                         "proj4": area.proj4_string,
                                         "shape": (area.x_size, area.y_size)
                                         }
                        except AttributeError:
                            area_data = None

                        to_send = {"nominal_time": getattr(obj, "time_slot"),
                                   "uid": os.path.basename(fname),
                                   "uri": os.path.abspath(fname),
                                   "area": area_data,
                                   "productname": obj.info["productname"]
                                   }
                        # if self._topic is not None:
                        if self._topic is not None:
                            topic = self._topic
                            if area_data is not None:
                                topic = compose(topic,  area_data)
                            else:
                                topic = compose(topic, {'area_id': 'satproj'})
                            msg = Message(topic, "file", to_send)
                            pub.send(str(msg))
                            self.logger.debug("Sent message: %s", str(msg))
                        self.logger.info("Saved %s", fname)

                    del obj
                    obj = None
                    # After all the items have been processed, release the
                    # lock for the previous worker
                    if self.prev_lock is not None:
                        utils.release_locks([self.prev_lock],
                                            self.logger.debug,
                                            "Writer releses lock of "
                                            "previous worker: %s" %
                                            str(self.prev_lock))
                else:
                    time.sleep(1)

    def stop(self):
        """Stop writer."""
        self._loop = False

    @property
    def loop(self):
        """Property loop"""
        return self._loop
