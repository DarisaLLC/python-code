#!/usr/local/bin/python3

from numpy import *
a = arange(15).reshape(3, 5)

print("basics")
print(a)
print(a.shape)
print(a.ndim)
print(a.dtype.name)
print(a.itemsize)
print(a.size)
print(type(a))

b = array([6, 7, 8])
print(b)
print(type(b))

a = array([1,2,3,4])
b = array( [ (1.5,2,3), (4,5,6) ] )
c = array( [ [1,2], [3,4] ], dtype=complex )

print("array function")
print(a)
print(b)
print(c)

print("zeros, ones and empty")
print(zeros( (3,4) ))
print(ones( (2,3,4), dtype=int16 ))
print( empty([2,3]) ) # empty does not bother to initialize the cells, so you may find random values

print(arange( 0, 2, 0.3 ))
print(linspace( 0, 2, 9 ))
