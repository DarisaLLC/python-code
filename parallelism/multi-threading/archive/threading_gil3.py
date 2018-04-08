#!/usr/local/bin/python3

import threading
import time

def worker():
	print(threading.currentThread().getName(), 'starting')
	time.sleep(2)
	print(threading.currentThread().getName(), 'exiting')

def my_service():
	print(threading.currentThread().getName(), 'starting')
	time.sleep(3)
	print(threading.currentThread().getName(), 'exiting')	

t = threading.Thread(name="my_service", target=my_service)
w1 = threading.Thread(name="worker1", target=worker)
w2 = threading.Thread(target=worker)

t.start()
w1.start()
w2.start()
