#!/usr/bin/env python3 

import queue
import threading
import time

def worker():
    while True:
        print("checking if queue is empty")
        item = q.get() # block
        if item is None:
            break
        print("got: " + str(item))
        q.task_done()

q = queue.Queue()
threads = []
for i in range(1):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

time.sleep(10)

for item in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    q.put(item) # blocks
    print("put: " + str(item))
    time.sleep(2)

# block until all tasks are done
q.join()

# stop workers
for i in range(1):
    q.put(None)
for t in threads:
    t.join()
