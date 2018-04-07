#!/usr/local/bin/python3

# python has a built in class str
# double and single quote are acceptable for literals
# baskslash escapes work as is normal
# triple quotes and backslashes are used for multi-line strings
# immutable, like java
# characters accessed using [], zero indexed
# slices can extract substrings
# len() and [] work for any sequence, including strings, lists, etc.
# + concatenation
# no variables declaration, just assignment

s = "hi"
print(s[1])
print(len(s))
print(s + " there")

# str() conversion
pi = 3.14
text = "The value of pi is " + str(pi)

# for numbers // indicates integer division

# string methods " s.lower(), s.upper(). s.strip(). s.isalpha(), s.isdigit(), s.isspace()
# s.startswith("bla"), s.endswith("bla"), s.find("substring"), s.replace("old, "new")
# s.split("delimiter"), s.join(list) (uses as as joining delimiter)
# there is no special character class in python, they are just strings with length 1

# slices
# just like lists... see lists.py
# s[:n] + s[n:] == s

# string % formats a string using the falgs  %d, %s, %f and the matching values in a tuple on the right 
text = "%d aaa %s and %s" % (3, "bla", "bla")
print(text)

# strings in python are ascii by default, not unicode
# the u prefix makes a unicode literal
# unicode strings are of a different class, but share the same base class basestring with string

# if statement
# no braces for conditionals/loops
# rather python uses : and spaces to group statements
# also boolean tests for if don't need to be in parentheses
