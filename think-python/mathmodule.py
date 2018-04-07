#!/usr/bin/python

#a module is a file that contains related functions
#to use a module, we must import it
#this statement creates a module object called math
#module functions can be accessed using dot notation
import math

print(math)

radians = 0.7
height = math.sin(radians)
print(radians)
print(height)

degrees = 45
radians = degrees / 360 * 2 * math.pi
print(radians)
print(math.sin(radians))

print(math.sqrt(2)/2)
