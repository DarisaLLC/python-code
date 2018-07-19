#!/usr/bin/env python3

# In Python3, all classes extend object implicitly. In Python2, not extending
# object indicated an "old-style" class whil extending a new class indicated a
# "new-style" class. Old classes were all implemented using a built-in type
# called "instance", so type(x) would return "instance". New classes are purely
# user-defined types, so type(x) == x.__class__. There were differences between
# the two styles of classes relating to multiple inheritance, method resolution,
# but in Python3 developers should not need to know about "old-style" anymore.
# See https://stackoverflow.com/questions/54867/what-is-the-difference-between-old-style-and-new-style-classes-in-python
class Human:

    def __init__(self):
        self.name = "Jackson"
        self.head = self.Head()

    # The Head class is nested within the Human class. The main advantage of
    # nested classes is organization, classes which are only used by another
    # can be encapsulated by the using class, placing code closer to where it
    # will be read.
    class Head:

        def talk(self):
            return "talking..."

# An inner class in Python is a distinct entity which does not automatically get
# access to the outer class members in any special way. We show a way to
# implement an iterator with and without nested classes.
class Cats:

    def __init__(self):
        self.cats = []
        self.cur = 0

    def add(self, name):
        self.cats.append(name)
        return self

    def __iter__(self):
        return self

    def __next__(self):
        if self.cur >= len(self.cats):
            raise StopIteration
        self.cur += 1
        return self.cats[self.cur - 1]

class Dogs:

    class _iter:

        def __init__(self, dogs):
            self.dogs = dogs
            self.cur = 0

        def __next__(self):
            if self.cur >= len(self.dogs):
                raise StopIteration

            self.cur += 1
            return self.dogs[self.cur - 1]

    def __init__(self):
        self.dogs = []
        self.cur = 0

    def add(self, name):
        self.dogs.append(name)
        return self

    def __iter__(self):
        return Dogs._iter(self.dogs)

if __name__ == "__main__":
    j = Human()
    print(j.name)
    print(j.head.talk())

    h = Human.Head()
    print(h.talk())
