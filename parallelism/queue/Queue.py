import threading
from collections import deque


class Queue(object):

    def __init__(self, maxsize=0):
        self.maxsize = maxsize
        self._init()

        self.mutex = threading.Lock() # accessing queue
        self.not_empty = threading.Condition(self.mutex) # signal get
        self.not_full = threading.Condition(self.mutex) # signal put
        self.all_tasks_done = threading.Condition(self.mutex) # signal waiting threads

        self.unfinished_tasks = 0

    def task_done(self):
        with self.all_tasks_done: # acquires all_tasks_done cv's mutex
            unfinished = self.unfinished_tasks - 1
            if unfinished < 0:
                raise Exception("task_done() called too many times")
            elif unfinished == 0:
                self.all_tasks_done.notify_all() # notifies all threads waiting on the queue
            self.unfinished_tasks = unfinished
            # releases cv's mutex
            # it doesn't seem like waiting threads need this cv after all tasks are done

    def join(self):
        with self.all_tasks_done: # acquires all_tasks_done cv mutex
            while self.unfinished_tasks:
                self.all_tasks_done.wait() # wait until all_tasks_done is signalled and task count is 0

    def qsize(self):
        with self.mutex:
            return self._qsize()

    def empty():
        with self.mutex:
            return not self._qsize()

    def full(self):
        with self.mutex:
            return 0 < maxsize <= self._qsize() # possible race condition

     def put(self, item, block=True, timeout=None):
        with self.not_full: # acquires not_full cv's mutex
            if self.maxsize > 0:
                if not block:
                    if self._qsize() >= self.maxsize:
                        raise Exception("Queue full")
                elif timeout is None:
                    while self._qsize() >= self.maxsize:
                        self.not_full.wait() # wait until queue is not full
                elif timeout < 0:
                    raise Exception("'timeout' must be a non-negative number")
                else:
                    endtime = time() + timeout
                    while self._qsize() >= self.maxsize:
                        remaining = endtime - time()
                        if remaining <= 0.0:
                            raise Exception("Queue full")
                        self.not_full.wait(remaining)
            self._put(item)
            self.unfinished_tasks += 1
            self.not_empty.notify() # a thread will only be waiting on not_empty if it try to get() while the queue was empty

    def get(self, block=True, timeout=None):
        with self.not_empty:
            if not block:
                if not self._qsize():
                    raise Exception("Queue empty")
            elif timeout is None:
                while not self._qsize():
                    self.not_empty.wait()
            elif timeout < 0:
                raise Exception("'timeout' must be a non-negative number")
            else:
                endtime = time() + timeout
                while not self._qsize():
                    remaining = endtime - time()
                    if remaining <= 0.0:
                        raise Exception("Queue empty")
                    self.not_empty.wait(remaining)
            item = self._get()
            self.not_full.notify()
            return item

    def put_nowait(self, item):
        return self.put(item, block=False)

    def get_nowait(self):
        return self.get(block=False)

    def _init(self):
        self.queue = deque()

    def _qsize(self):
        return len(self.queue)

    def put(self, item):
        self.queue.append(item)

    def get(self):
        return self.queue.popleft()
