#!/usr/local/bin/python3

import codecs

# python's hash table is known as a dictionary
# kvp's written within braces, e.g. dict = {key1:value1, key2:value2}
# empty dict is {}
# strings, numbers and tuples (immutable) work as keys

# build up pattern
dict = {}
dict['a'] = "alpha"
dict['g'] = "gamma"
dict['o'] = "omega"

print(dict)

print(dict['a'])
dict['a'] = 6
print('a' in dict)
print(dict.get('z'))

# for iterates through the keys of a dict in arbitrary order
# dict.keys() and dict.values() return lists of keys and values
# dict.items() returns 2-tuples
for key in dict: print(key)
print(dict.keys())
print(dict.values())
print(dict.items())

for key in sorted(dict.keys()):
    print(type(key))
 
for k, v in dict.items(): print(k, v)

# formatting using %
hash = {}
hash["word"] = "garfield"
hash["count"] = 42
s = "I wamt %(count)d copies of %(word)s" % hash
print(s)

# open() returns a file handle for I/O
f = open("lists.py", "rU")
for line in f:
    print(line)
f.close()

# codecs module provides support for reading unicode files
# use codecs.open(name, flags, unicode_encoding) 
