#!/usr/bin/env python3

import os
import sys
import time
import signal

def daemonize(stdout="/dev/null", stderr=None, stdin="/dev/null", pidfile=None):
    try:
        pid = os.fork()
        if pid != 0:
            sys.exit(0)
    except OSError as e:
        sys.exit("first fork failed")

    os.chdir("/")
    os.umask(0)
    os.setsid()

    try:
        pid = os.fork()
        if pid != 0:
            sys.exit(0)
    except OSError as e:
        sys.exit("second fork failed")

    # why not default stderr to /dev/null
    if not stderr:
        stderr = stdout

    si = open(stdin, "r")
    so = open(stdout, "a+")
    se = open(stderr, "a+")

    pid = str(os.getpid())
    print("started with pid: {}".format(pid), file=sys.stdout)

    if pidfile:
        open(pidfile, "w+").write("{}\n".format(pid))

    os.dup2(si.fileno(), sys.stdin.fileno())
    os.dup2(so.fileno(), sys.stdout.fileno())
    os.dup2(se.fileno(), sys.stderr.fileno())

# co-ordinate pidfile defaults
def start_stop(stdout="/dev/null", stderr=None, stdin="/dev/null", pidfile="pid.txt"):
    if len(sys.argv) > 1:
        action = sys.argv[1]

        try:
            pf = open(pidfile, "r")
            pid = int(pf.read().strip())
            pf.close()
        except IOError:
            pid = None

        if action == "stop" or action == "restart":
            if not pid:
                sys.exit("could not stop, no pidfile: {}".format(pidfile))

            try:
                while 1:
                    os.kill(pid, signal.SIGTERM)
                    time.sleep(1)
            except OSError as e:
                msg = str(e)
                if msg.find("No such process") > 0:
                    os.remove(pidfile)
                    if action == "stop":
                        sys.exit(0)
                    action = "start"
                    pid = None
                else:
                    sys.exit(msg)

        if action == "start":
            if pid:
                sys.exit("start aborted since pidfile exists: {}".format(pidfile))
            daemonize(stdout, stderr, stdin, pidfile)
            return

        sys.exit("usage: {} start|stop|restart".format(sys.argv[0]))

def test():
    print("message to stdout")
    print("message to stderr")

    c = 0
    while True:
        print(c, time.ctime())
        c += 1
        time.sleep(1)

if __name__ == "__main__":
    start_stop(stdout='/tmp/deamonize.log', pidfile='/tmp/deamonize.pid')
    test()
