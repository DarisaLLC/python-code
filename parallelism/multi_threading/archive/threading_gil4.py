#!/usr/local/bin/python3

import logging
import threading
import time

logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

def worker():
	logger.info("Starting")
	time.sleep(2)
	logger.info("Exiting")

def my_service():
	logger.info("Starting")
	time.sleep(3)
	logger.info("Exiting")

t = threading.Thread(name="my_service", target=my_service)
w1 = threading.Thread(name="worker1", target=worker)
w2 = threading.Thread(target=worker)

t.start()
w1.start()
w2.start()
