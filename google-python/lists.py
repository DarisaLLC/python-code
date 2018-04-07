#!/usr/local/bin/python3

# built in list type
# literals written in []
# similar to strings, use len() to get length and [] to access zero-indexed data 
colors = ["red", "blue", "green"]
print(colors[0])
print(len(colors))

# lists are objects and = assignment makes two variables point to the same memory block
b = colors

# empty list []
empty = []

# append lists with +
a = [1, 2] + [3, 4]
print(a)

# for construct iterates over elements of list 
squares = [1, 4, 9, 16]
sum = 0
for num in squares:
    sum += num
print(sum)

# in checks element existence 
names = ["larry", "curly", "moe"]
print("curly" in names)

# note that strings are considered lists of characters
s = "jackson"
for c in s: print(c)

# range(n) returns integers from 0 to n-1 
# range(a, b) returns a, a+1, ... , b-1
for i in range(5):
    print(i)

# python also has while, break and continue
i = 0
while i < len(a):
  print(a[i])
  i = i+2

# list methods : append, extend, insert, index, remove, sort, reverse, pop, etc.
list = ['larry', 'curly', 'moe']
list.append('shemp')         ## append elem at end
list.insert(0, 'xxx')        ## insert elem at index 0
list.extend(['yyy', 'zzz'])  ## add list of elems at end
print (list)  ## ['xxx', 'larry', 'curly', 'moe', 'shemp', 'yyy', 'zzz']
print (list.index('curly'))    ## 2
list.remove('curly')         ## search and remove that element
list.pop(1)                  ## removes and returns 'larry'
print (list)  ## ['xxx', 'moe', 'shemp', 'yyy', 'zzz']

# build up using append or extend
list = []
list.append("jackson")

# slices (like with strings)
list = ['a', 'b', 'c', 'd']
print(list[1:-1])

list[0:2] = "replacement"
print(list)
