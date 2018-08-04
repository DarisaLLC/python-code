#!/usr/bin/env python3

import daemon

def hi_forever():
    while True:
        print("hello world")

with daemon.DaemonContext() as context:
    hi_forever()
