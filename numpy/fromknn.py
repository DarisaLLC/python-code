#!/usr/local/bin/python3

import numpy as np

x = np.arange(16.0).reshape(4, 4)

# splits array into sub-arrays vertically (first axis)
print(np.vsplit(x, 2))

# splits array into sub-arrays horizontally (second axis)
print(np.hsplit(x, 2))

# create a new list which repeats each element of the old list a number of times 
k = np.arange(10)
print(np.repeat(k, 3))
