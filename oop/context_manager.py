#!/usr/bin/env python3

"""
Context Manager (class style):

This is a regular python obejct with special methods __enter__ and __exit__.
First the obect is instantiated, then the returv value of __enter__ is assigned
to f. On leaving the block, __exit__ is called.
"""
class CustomOpen:

    def __init__(self, path, flag):
        self.file = open(path, flag)

    def __enter__(self):
        return self.file

    def __exit__(self, ctx_type, ctx_value, ctx_traceback):
        self.file.close()

if __name__ == "__main__":

    with CustomOpen("dict.py", "r") as f:
        s = f.read()
        print(s)
