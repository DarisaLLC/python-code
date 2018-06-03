# #!/usr/local/bin/python3
#
import threading

"""
starting threads and passing arguments
"""

def worker1(num):
    print("Worker: {}".format(num))

threads = []
for i in range(5):
    t = threading.Thread(target=worker1, args=(i,))
    threads.append(t)
    # t.start()

"""
thread name in log messages
"""

import logging
#
logging.basicConfig(
    level=logging.DEBUG,
    format="[%(levelname)s] (%(threadName)-10s) %(message)s"
)

"""
determining current thread
"""

import time

def worker2():
    logging.debug("starting " + threading.currentThread().getName())
    time.sleep(2)
    logging.debug("exiting" + threading.currentThread().getName())

def my_service():
    logging.debug("starting " + threading.currentThread().getName())
    time.sleep(3)
    logging.debug("exiting " + threading.currentThread().getName())

t = threading.Thread(name="my_service", target=my_service)
w = threading.Thread(name="worker2", target=worker2)
w2 = threading.Thread(target=worker2) # default thread name

w.start()
w2.start()
t.start()

"""
daemon vs non-daemon
"""

def daemon():
    logging.debug("Starting")
    time.sleep(2)
    logging.debug("Exiting")

d = threading.Thread(name="daemon", target=daemon)
d.setDaemon(True)

def non_daemon():
    logging.debug("Starting")
    logging.debug("Exiting")

t = threading.Thread(name="non-daemon", target=non_daemon)

d.start()
t.start() # main and non-daemon threads do not need to wait for daemons to finish

"""
joining and checking if a thread is alive
"""

d.join(1) # main thread waits for 1 second
print(d.isAlive())
t.join()

"""
enumerating active threads
"""

import random

def worker3():
    t = threading.currentThread()
    pause = random.randint(1,5)
    logging.debug("sleeping %s", pause)
    time.sleep(pause)
    logging.debug("ending")

for i in range(3):
    t = threading.Thread(target=worker3)
    t.setDaemon(True)
    # t.start()

main_thread = threading.currentThread()
# for t in threading.enumerate():
    # if t is main_thread:
    #     continue
    # logging.debug("joining %s", t.getName())
    # t.join()

"""
subclassing Thread

At startup, Thread does some basic initialization and then calls its run() method,
which in turn calls the target function. A Thread subclass should override run()
todo whatever is necessary.
"""

class MyThread(threading.Thread):
    def run(self):
        logging.debug("running")

for i in range(5):
    t = MyThread()
    t.start()

class MyThreadWithArgs(threading.Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None):
        threading.Thread.__init__(self, group=group, target=target, args=args, kwargs=kwargs, name=name)
        self.args = args
        self.kwargs = kwargs

    def run(self):
        logging.debug("[MyThreadWithArgs] running with %s and %s", self.args, self.kwargs)

for i in range(5):
    t = MyThreadWithArgs(args=(i,), kwargs={'a':'A', 'b':'B'})
    t.start()

"""
timer threads
"""

def delayed():
    logging.debug("worker running")

t1 = threading.Timer(3, delayed)
t1.setName("t1")
t2 = threading.Timer(3, delayed)
t2.setName("t2")

logging.debug("start timers")
t1.start()
t2.start()

logging.debug("waiting before cancelling %s", t2.getName())
time.sleep(2)
logging.debug("cancelling %s", t2.getName())
t2.cancel()
logging.debug("cancelled")


"""
signalling between threads
"""

def wait_for_event(e):
    logging.debug("wait_for_event starting...")
    event_is_set = e.wait()
    logging.debug("event set %s", event_is_set)

def wait_for_event_timeout(e, t):
    while not e.isSet():
        logging.debug("wait_for_event_timeout starting...")
        event_is_set = e.wait(t)
        logging.debug("event set %s", event_is_set)
        if event_is_set:
            logging.debug("processing event")
        else:
            logging.debug("doing other work")

e = threading.Event()

t1 = threading.Thread(name="block", target=wait_for_event, args=(e,))
t1.start()

t2 = threading.Thread(name="non-block", target=wait_for_event_timeout, args=(e, 2))
t2.start()

logging.debug("waiting before calling event.set()")
time.sleep(3)

e.set()
logging.debug("event is now set")

"""
controlling access to resources
"""

class Counter (object):
    def __init__(self, start=0):
        self.lock = threading.Lock()
        self.value = start
    def increment(self):
        logging.debug("waiting for lock...")
        self.lock.acquire()
        try:
            logging.debug("acquired lock...")
            self.value = self.value + 1
        finally:
            self.lock.release()

def worker4(c):
    for i in range(2):
        pause = random.random()
        logging.debug("sleeping %0.02f", pause)
        time.sleep(pause)
        c.increment()
    logging.debug("done")

counter = Counter()
for i in range(2):
    t = threading.Thread(target=worker4, args=(counter,))
    t.start()

logging.debug("waiting for worker threads")
main_thread = threading.currentThread()
for t in threading.enumerate():
    if t is not main_thread:
        t.join()

logging.debug("Counter: %d", counter.value)

def lock_holder(lock):
    logging.debug("starting...")
    while True:
        lock.acquire()
        try:
            logging.debug("holding")
            time.sleep(0.5)
        finally:
            logging.debug("not holding")
            lock.release()
        time.sleep(0.5)

def worker5(lock):
    logging.debug("starting...")
    num_tries = 0
    num_acquires = 0
    while num_acquires < 3:
        time.sleep(0.5)
        logging.debug("trying acquire")
        have_it = lock.acquire(0)
        try:
            num_tries += 1
            if have_it:
                logging.debug("iteration %d: acquired", num_tries)
                num_acquires += 1
            else:
                logging.debug("iteration %d: not acquired", num_tries)
        finally:
            if have_it:
                lock.release()
    logging.debug("done after %d iterations", num_tries)

lock = threading.Lock()

holder = threading.Thread(target=lock_holder, args=(lock,), name="LockHolder")
holder.setDaemon(True)
holder.start()

worker = threading.Thread(target=worker5, args=(lock,), name="Worker")
worker.start()

"""
locks as context managers
"""

def worker_with(lock):
    with lock:
        logging.debug("lock acquired using 'with'")

def worker_no_with(lock):
    lock.acquire()
    try:
        logging.debug("lock acquired directly")
    finally:
        lock.release()

lock = threading.Lock()
w = threading.Thread(target=worker_with, args=(lock,))
nw = threading.Thread(target=worker_no_with, args=(lock,))

w.start()
nw.start()

"""
synchronizing threads
"""

def consumer(cond):
    logging.debug("starting consumer...")
    t = threading.currentThread()
    with cond:
        cond.wait()
        logging.debug("resource is available to consumer")

def producer(cond):
    logging.debug("starting producer...")
    with cond:
        logging.debug("making resource available")
        cond.notifyAll()

condition = threading.Condition()
c1 = threading.Thread(name="c1", target=consumer, args=(condition,))
c2 = threading.Thread(name="c2", target=consumer, args=(condition,))
p = threading.Thread(name="p", target=producer, args=(condition,))

c1.start()
time.sleep(2)
c2.start()
time.sleep(2)
p.start()

"""
limiting cocurrent access to resources
"""

class ActivePool(object):
    def __init__(self):
        # super(ActivePool, self).__init__()
        self.active = []
        self.lock = threading.Lock()
    def makeActive(self, name):
        with self.lock:
            self.active.append(name)
            logging.debug("running %s", self.active)
    def makeInactive(self, name):
        with self.lock:
            self.active.remove(name)
            logging.debug("running %s", self.active)

def worker(s, pool):
    logging.debug("waiting to join the pool")
    with s:
        name = threading.currentThread().getName()
        pool.makeActive(name)
        time.sleep(0.1)
        pool.makeInactive(name)

pool = ActivePool()
s = threading.Semaphore(2)
for i in range(6):
    t = threading.Thread(target=worker, name=str(i), args=(s, pool))
    t.start()

"""
thread specific data
"""

def show_value(data):
    try:
        val = data.value
    except AttributeError:
        logging.debug("no value yet")
    else:
        logging.debug("value=%s", val)

def worker6(data):
    show_value(data)
    data.value = random.randint(1, 100)
    show_value(data)

local_data = threading.local()

show_value(local_data)
local_data.value = 1000
show_value(local_data)

for i in range(2):
    t = threading.Thread(target=worker6, args=(local_data,))
    t.start()
