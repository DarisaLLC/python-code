#!/usr/local/bin/python3

import sys

"""
generators vs coroutines :
-generators are data producers 
-coroutines are data consumers 
"""

# typical generator 
def fib():
    a, b = 0, 1
    while True: 
        yield a
        a, b = b, a+b

# for i in fib():
#     print(i)

# a coroutine is simply a generator which also takes input
def grep(pattern):
    print("Searching for", pattern)
    while True:
        line = yield
        if pattern in line:
            print(line)

search = grep("coroutine")
search.send(None)
search.send("I love you.")
search.send("Don't you love me?")
search.send("I love coroutines instead!")
search.close() # close the coroutine

sys.exit()

"""
threads (and processes) are the traditional way to handle concurrency, but they are not perfect 
-threads need to be synchronized, which may recquire complex code
-threads recquire non-trivial memory, which may lead to resource starvation at high volumes

coroutines are an alternative when it comes to concurrent operations 
"""

# coroutines work by enabling code consuming a generator to send a value back into the generator after each yield
# the generator reveives the input as the result of the last yield operation 
# the cost of starting a generator coroutine is a function call
# once active, they take up less than 1KB of memory 
def my_cr():
    while True:
        rcvd = yield
        print("received : " + rcvd) 

it = my_cr()
it.send(None) # move generator to first yield 
it.send("first")
it.send("second")

def minimize():
    current = yield 
    while True: 
        value = yield current
        current = min(value, current)

it = minimize()
it.send(None) # move generator to first yield

print(it.send(10)) # generator gets input and returns current
print(it.send(4)) # update current and then yield it
print(it.send(-1)) # and again...

"""
code consuming the generators can take action after each yield
the output can be used to call other functions and call other data structures 
it can also advance other generator functions 
by advancing multiple generators we achieve (user controlled) concurrency 
"""

ALIVE = "*"
EMPTY = "-"

