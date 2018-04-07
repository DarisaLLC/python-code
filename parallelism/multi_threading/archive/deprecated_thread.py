#!/usr/local/bin/python3

import _thread as thread
import time

def print_time(thread_name, delay):
	count = 0
	while count < 5:
		time.sleep(delay)
		count += 1
		print("%s: %s" % (thread_name, time.ctime(time.time())))

try:
	thread.start_new_thread(print_time, ("Thread-1", 2))
	thread.start_new_thread(print_time, ("Thread-2", 4))
except Exception as e:
	print("Error: unable to start thread")
	print(e)	

while 1:
	pass
