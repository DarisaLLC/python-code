#!/usr/bin/env python3

class A:

    # When methods are invoked, the object is implicitly passed in.
    def foo(self, x):
        print("executing foo ({}, {})".format(self, x))

    # When class methods are invoked, the class is implicitly passed in.
    @classmethod
    def class_foo(cls, x):
        print("executing class_foo ({}, {})".format(cls, x))

    # Static methods are like functions grouped in a class, neither object nor
    # class is passed in.
    @staticmethod
    def static_foo(x):
        print("executing static_foo ({})".format(x))

if __name__ == "__main__":
    a = A();
    a.foo(1)
    A.class_foo(2)
    a.static_foo(3)
