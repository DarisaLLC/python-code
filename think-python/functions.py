#!/usr/bin/python

#the following function definition identigies the sequence of statements to be executed when the function is called
#defining a function declares a function object with the same name
#function definitions must precede their first invocation
#when an error occurs, the python interpreter prints a traceback which lists main and each subsequent function call

def print_lyrics():
	print ("I'm a lumberjack, and I'm okay")
	print ("I sleep all night and I work all day")

def repeat_lyrics():
	print_lyrics()
	print_lyrics()

def print_twice(s):
	print(s)
	print(s)

print (print_lyrics)

repeat_lyrics()

print_twice("hello")

#expression arguments are evaluated once only
print_twice(type(2))
