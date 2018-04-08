#!/usr/local/bin/python3

import math

"""
Normal functions which extract primes from a list.
"""

def get_primes1(input_list):
    result_list = []
    for element in input_list:
        if is_prime(element):
            result_list.append(element)
    return result_list

def get_primes2(input_list):
    return [x for x in input_list if is_prime(x)]

def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0:
                return False
        return True
    else:
        return False 

# print(get_primes1([3, 2, 12, 28, 71, 15, 5]))

"""
What if we want to find all the primes from 2 to infinity? 
The input would not fit in memory.
So we want a "function" which returns the next value each time
"""

# generator functions contain the "yield" keyword
def get_primes3(n):
    while True:
        if is_prime(n):
            yield n
        n += 1

def solve_number_10():
    total = 2
    for next_prime in get_primes3(2):
        if next_prime < 2000000:
            total += next_prime
        else:
            print(total)
            return

# generator.send sends and recieves data 
def print_successive_primes(iterations, base=10):
    g = get_primes3(base) # generators can be assigned to a variable
    g.send(None)
    for power in range(iterations):
        print(g.send(base ** power))

print_successive_primes(10)

"""
recap : 

-generators simplify creation of iterators
-a generator produces a sequence of results 
"""

def yrange(n):
    i = 0
    while i < n:
        yield i
        i += 1

# each time yield executes a new value is generated
# as with an iterator, an exception is thrown 
y = yrange(3) # creates a generator
print(y.__next__())
print(y.__next__())
print(y.__next__())

# when a generator function is called, it returns a generator object 
# __next__() gives the value at the next yield statement

def foo():
    print("begin")
    for i in range(3):
        print("before yield")
        yield i
        print("after yield")
    print("end")

f = foo() # generator object
print(f.__next__()) 
print(f.__next__())

# infinite sequence
def integers():
    i = 1
    while True: 
        yield i
        i += 1

def squares():
    # the generator class also implements the iterator interface
    for i in integers():
        yield i * i 

def take(n, seq):
    seq = iter(seq)
    results = []
    try:
        for i in range(n):
            results.append(seq.__next__())
    except StopIteration:
        pass 
    return results    

print(take(5, squares()))

# generator expressions return a generator (analagous to list comprehension)
a = (x*x for x in range(10))
s = sum(a)
print(s)

# e.g. reading multiple files 

def cat(fnames):
    for f in fnames:
        for line in open(f):
            print(line)

def grep(pattern, fnames):
    for f in fnames:
        for line in open(f):
            if pattern in line:
                print(line)

def readfiles(fnames):
    for f in fnames:
        for line in open(f):
            yield line

def grep(pattern, lines):
    return(line for line in lines if pattern in line)

# operates on an iterable (could be list, iterable, generator)
def printlines(lines):
    for line in lines:
        print(line)

def main(pattern, fnames):
    lines = readfiles(fnames) # generator object
    lines = grep(pattern, lines) # generator object of search results
    printlines(lines)
