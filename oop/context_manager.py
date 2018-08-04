#!/usr/bin/env python3

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
