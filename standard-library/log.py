import logging

"""
logging is the practice of tracking events which happen when software runs, they
describe that state of a program any error conditions, log messages have an
importance which the developer ascribes, i.e. level

logging (module) provides convenience functions debug(), info(), warning(),
error() and critical()

ordinary usage - print()
* detailed operation details - logging.debug()
* normal operation monitoring - logging.info()
* warning regarding a runtime event - logging.warning()
* report suppression of an error - logging.error()
* report a runtime error - raise and Exception

the default level is WARNING, meaning only events of this level or above will be
tracked
"""

# by default, warning will be printed to terminal
# logging.warning("watch out")
# logging.info("normal stuff")

# must be the first logging statement
# filemode is append by default, we can also overwrite
logging.basicConfig(filename="example.log", filemode="w", format="[%(levelname)s] %(message)s", level=logging.DEBUG)

logging.debug("debug to file")
logging.info("info to file")
logging.warning("warning to file")
