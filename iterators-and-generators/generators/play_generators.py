#!/usr/bin/env python3

import math
import random

"""
using yield in a function causes it to become a generator function 
a generator function returns a generator object
a generator object extends iterator and returns values via next() or __next__()
yield both provides a value and yields control to the calling code
after traversing all items, the generator raises a StopIteration exception (like normal iterators)
"""

def g1(n):
    if n < 0: return None 
    i = 0
    while i < n: 
        yield i
        i += 1

# g = g1(10)
# print("type of g: {}".format(type(g)))

"""
yield can both receive a value and provide one at the same time 
"""
def is_prime(x):
    if x == None: return False
    if x < 3: return False
    if x % 2 == 0: return False
    for i in range(3, int(math.sqrt(x))+1, 2):
        if x % i == 0: return False
    return True

# print(is_prime(10))

def get_primes(start):
    x = start 
    while True:
        if is_prime(x):
            yield x
        x += 1

def get_ge_prime(n):
    while True: 
        if is_prime(n):
            """
            the first time you send None, the generator is initialized to the beginning of the first yield statement 
            the initial value of n is yielded and n is set to None   
            subsequently, n receives the sent value and iterates until it yields the result
            """
            n = yield n
        n += 1

# for p in get_primes(3):
#     if p > 1000: break
#     print(p)
     
# g = get_ge_prime(100) # creates a generator object starting from 100
# print(g.__next__()) # takes None and yields 101 
# print(g.__next__()) # error when trying to increment None 

"""
def successive_primes(iterations, base=10):
    g = get_ge_prime(random.randint())
    for i in range(0, iterations):
        print(g.send(base**iterations))
"""    

"""
def print_successive_primes(iterations, base=10):
    prime_generator = get_ge_prime(base)
    # print(prime_generator.send(None))
    for power in range(iterations):
        print(prime_generator.send(base ** power))

print_successive_primes(5)
"""

# ge = get_ge_prime(10)
# print(ge.send(None))

def jumping_range(n):
    i = 0
    while i < n:
        jump = yield i
        if jump is None: jump = 1
        i += jump

g = jumping_range(15)

# notice that calling __next__() implicitly sends None 
print(next(g))

print(g.send(2))
print(next(g)) # sends None
print(g.send(-1))
print(g.send(None))
for i in g: print(i)
