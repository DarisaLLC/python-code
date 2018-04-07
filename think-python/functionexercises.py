#!/usr/bin/python

print(len('jackson'))

def right_justify(s):
	print(" "*69 + s)

def do_twice(f, arg):
	f(arg)
	f(arg)

def print_spam(arg):
	print (arg)

def print_twice(arg):
	print (arg)
	print (arg)

def do_four(f, arg):
	do_twice(f, arg)
	do_twice(f, arg)

right_justify("jackson")
do_twice(print_twice, "argument")

print("\n")
do_four(print_spam, "argument")

#prints a grid
def print_header():
	print("+", "-"*4, "+", "-"*4, "+")

def print_row():
	print("|", " "*4, "|", " "*4, "|")

print("\n")
print_header()
print_row()
print_row()
print_row()
print_row()
print_header()
print_row()
print_row()
print_row()
print_row()
print_header()
