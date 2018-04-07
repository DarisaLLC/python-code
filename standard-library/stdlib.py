#!/usr/local/bin/python3

"""
Useful Python modules/packages
Note : dir(module) and help(module) describe a module
"""

"""
1. os - interact with operating system
"""

import os

cwd = os.getcwd() # the working directory dynamically associated with a process

os.chdir("/Users/jguo")
print("changed directory to : " + os.getcwd())

os.chdir(cwd)
print("changed back to : " + cwd)

if not os.path.exists(cwd + "/stdlib_test"):
    os.system("mkdir stdlib_test")
    print("made directory stdlib_test")

"""
2. shutil - file and directory management
"""

import shutil

shutil.copyfile("data.txt", "data_copy.txt")
shutil.move("data_copy.txt", "data_copy_renamed.txt")
print("copied data.txt to data_copy.txt then renamed to data_copy_renamed.txt")

"""
3. glob - globbing patterns
"""

import glob

tf = glob.glob("*.txt")
print("globbed text files : " + str(tf))

"""
4. sys - interact with python interpreter
"""

import sys

print("command line arguments : " + str(sys.argv)) # alternatives are getopt and argparse
sys.stderr.write("stderr : writing an error message even if stdout is redirected\n")

"""
5. re - regex pattern matching
"""

import re

p = re.findall(r"\bf[a-z]*", "which foot or hand fell fastest") # raw strings disable escape interpretation
print("words starting with f : " + str(p))

s1 = re.sub(r"(\b[a-z]+) \1", "double", "cat in the the hat")
print("replaced double words : " + s1)

s2 = "tea for two".replace("too", "two")
print(s2)

"""
6. math - uses underlying C math functions
"""

import math

print("cos of pi/4 : " + str(math.cos(math.pi/4)))
print("log2 of 1024 : " + str(math.log(1024, 2)))

"""
7. random - random numbers
"""

import random

c = random.choice(["a", "b", "c"])
print("random choice : " + c)

sp = random.sample(range(100), 5)
print("random sample : " + str(sp))

rd = random.random()
print("random float between 0 and 1 (exclusive) : " + str(rd))

rg = random.randrange(6)
print("random number from range 0 to 6 (exclusive) : " + str(rg))

"""
8. statistics - statistical functions
"""

import statistics # also see scipy

data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
mean = statistics.mean(data)
median = statistics.median(data)
variance = statistics.variance(data)
print("mean {}, median {}, variance {}".format(mean, median, variance))

"""
9. urllib - http library
"""

from urllib.request import urlopen

with urlopen("http://tycho.usno.navy.mil/cgi-bin/timer.pl") as resp:
    for line in resp:
        line = line.decode("utf-8") # binary data to text
        if "EST" in line or "EDT" in line:
            print(line)

"""
10. smtplib - sending mail (requires running mail server)
"""

# import smtplib
# server = smtplib.SMTP("localhost")
# server.sendmail("jackson.guo@zerogravitylabs.ca", """
# To: j84guo@edu.uwaterloo.ca
# From: jackson.guo@zerogravitylabs.ca
#
# Test message from python client.
# """)
# server.quit()

"""
11. datetime - dates and times
"""

from datetime import date

now = date.today()
print("current date : " + str(now))

bd = date(1997, 2, 25)
print("birth date : " + str(bd))

age = now - bd
print("age in days : " + str(age.days))

"""
12. zlib, gzip, lzma - data compression
"""

import zlib

s = b"aaaaaaa aaaaaaaa aaaaaaa aaa aa aaaa aaaaaaa"
print("uncompressed size : " + str(len(s)))

c = zlib.compress(s)
print("compressed size : " + str(len(c)))

s = zlib.decompress(c)
print(len(s))
