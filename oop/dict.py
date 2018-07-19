#!/usr/bin/env python3

# In Python, object instance members are really dictionaries. This is why
# objects can have attributes dynamically added.
class Foo:
    def __init__(self, name=""):
        self.name = name

class Person:
    pass

def print_people():
    # open() returns a file object
    # file objects have read(), which reads the whole file or some bytes
    # readLine() which returns one line
    # readLines() which returns all lines in a list
    # loop (using __iter__() and __next__()) through all lines
    f = open("people.txt", mode="rt")
    people = []

    for l in f:
        people.append(Person())
        es = l.split(",")
        p = []
        for e in es:
            p.append(e.split("="))
        people[-1].__dict__ = dict(p)

    for person in people:
        print(person.__dict__)

if __name__ == "__main__":
    f = Foo("Anne")
    print(f.name)
    print(f.__dict__["name"])
    print(f.__dict__)

    print_people()
