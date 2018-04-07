#!/usr/local/bin/python3

import os.path

# basic write and read
with open("out.txt", "w") as f:
    f.write("Writing from files.py")
with open("out.txt", "r") as f:
    contents = f.read()
print(contents)

# buffered (by line) reading
with open("data.txt") as f:
    for line in f:
        print(line)

# check if path exists
path_to_file = "data.txt"
if(os.path.isfile(path_to_file)):
    print(path_to_file + " exists")

# relative to absolute path
abs_path = os.path.abspath("../opencv/image-and-video/filevideo.py") # from current working directory
print(abs_path)

# file name from path
filename = os.path.basename(abs_path)
print(filename)

# directory name from path
dirname = os.path.dirname(abs_path)
print(dirname)

# current directory
cwd = os.getcwd()
print(cwd)

# script directory
sd = os.path.dirname(os.path.realpath(__file__))

# list files 
ls = os.listdir(sd)
print(ls)

# list files recursively
path = "/tmp"

for root, directories, filenames in os.walk(path):
    for d in directories:
        print(os.path.join(root, d))
    for f in filenames:
        print(os.path.join(root,filename))
