#!/usr/bin/env python3

# An exception object represents an event which occurs during the execution of
# a program that disrupts the normal flow of execution, raised when a python
# application encounters a situation it cannot cope with. Exceptions must be
# handled, or the program will quit.
#
# Standard exceptions include:
# Exception (base class)
# StopIteration
# ArithmeticError
# AttributeError, etc.
#
# Exceptions must be caught in a try/except block, which optionally has finally
# or else blocks at the end.
#
# Note that many standard python exceptions derive from StandardError (child of
# exception) and so include Error in their name.
try:
    file = open("some_non_existent_file", "rt")
    try:
        lines = file.readLines()
    finally:
        print("Closing file.")
        file.close()
except Exception:
    print("Caught an exception.")
finally:
    print("Executing finally block.")

# Of course, a more elegant way to do this is.
try:
    with open("some_non_existent_file", "rt") as file:
        lines = file.readLines()
except Exception:
    print("Error opening and reading file.")
