#!/usr/bin/env python3

import os
import sys

umask = 0
work_dir = "/"
max_fd = 1024
redirect_to = os.devnull

def createDaemon():
    try:
        pid = os.fork()
    except OSError as e:
        raise e

    if pid == 0:
        os.setsid()

        try:
            pid = os.fork()
        except OSError as e:
            raise e

        if pid == 0:
            os.chdir(work_dir)
            os.umask(umask)
        else:
            os._exit(0)
    else:
        os._exit(0)

    import resource

    n = resource.getrlimit(resource.RLIMIT_NOFILE)[0]
    if n == resource.RLIM_INFINITY:
        n = max_fd

    for i in range(0, n):
        try:
            os.close(i)
        except OSError:
            pass

    os.open(redirect_to, os.RDWR)

    os.dup2(0, 1)
    os.dup2(0, 2)

    return 0

if __name__ == "__main__":
    print("creating daemon...")
    rc = createDaemon()

    params = """
    return code: {}
    pid: {}
    ppid: {}
    gid: {}
    sid: {}
    uid: {}
    euid: {}
    rgid: {}
    egid: {}
    """.format(rc, os.getpid(), os.getppid(), os.getpgrp(), os.getsid(0), os.getuid(), os.geteuid(), os.getgid(), os.getegid())

    with open("~/createDaemon.log", "w") as file:
        file.write(params + "\n")

    sys.exit(rc)
