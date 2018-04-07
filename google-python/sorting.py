#!/usr/local/bin/python3

# sorted(list) returns a new sorted list without modifying the original
# optional argument reverse=True
# list.sorted() is an older alternative
a = [5, 1, 4, 3]
print(sorted(a))
print(a)
print(sorted(a, reverse=True))

# custom sorting with key
# using optional parameter key=... which accepts a key function to transform each element before comparison
strs = ["ccc", "aaaa", "d", "bb"]
print(sorted(strs, key=len)) # string length is the proxy by which the list is sorted
print(sorted(strs, key=str.lower)) # upper and lower case treated the same

def myfunc(s):
    return s[-1] # last letter

print(sorted(strs, key=myfunc))

# tuples
# basically immutable lists
# items cannot be changed, but variables can be assigned to new tuples
t = (1, 2, 'hi')
print(len(t))
print(t[2])
t = (1, 2, 'bye') # new tuple object

# assigning a tuple to an identically sized tuple of variable names sets the cooresponding values
(x, y, z) = (42, 13, "hike")
print(z)

# list compression
nums = [1, 2, 3, 4]
squares = [n*n for n in nums]
print(squares)

strs = ["hello", "and", "goodbye"]
shouting = [s.upper()+"!!!" for s in strs]
print(shouting)

nums = [2, 8, 1, 6]
small = [ n for n in nums if n <= 2]
print(small)

fruits = ["apple", "cherry", "banana", "lemon"]
afruits = [s.upper() for s in fruits if 'a' in s]
print(afruits)
