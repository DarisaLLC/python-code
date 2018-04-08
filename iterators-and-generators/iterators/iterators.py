#!/usr/local/bin/python3

# loop through list elements, string characters, dict keys, file lines, etc.  using for 

for i in [1, 2, 3, 4]:
    print(i)

for c in "python3":
    print(c)

for k in {"x" : 1, "y" : 2}:
    print(k)

for line in open("data.txt"):
    print(line)

# objects which can be used in a for loop are iterables
# an iterable object also returns an iterator
# there are many functions which operate on iterables

print("".join(["a", "b", "c"]))
print("".join({"a":1, "b":2}))
print(list("python"))

# the built in function iter() takes an iterable and returns an iterator
# get the next item using next(iterator), an exception is thrown once at the last element
x = iter([1, 2])
print(next(x))
print(next(x))

# iterators are implemented as classes 
# here is an iterator which works like the built in xrange() function
class yrange(object):
    def __init__(self, n):
        self.i = 0
        self.n = n

    # __iter__() is the method which makes an object iterable
    # this method is called by iter()
    # as mentioned, an interator simply needs to have a __next__() function and 
    # raise an exception when done
    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.n: 
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()

l = list(yrange(5))
print(l)

s = sum(yrange(5))
print(s)

# the __iter__() method doesn't always have to return self, it just needs to be an interable

class zrange(object):
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return zrange_iter(self.n)

class zrange_iter(object):
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()

l = list(zrange(5))
print(l)
