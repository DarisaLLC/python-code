#!/usr/bin/env python3 

class A(object):

    sa = "static variable sa"

    def __init__(self):
        self.a = "instance variable a"

    def get_static(self):
        print("in Python, class (effectively static) variables can be accessed by self: {} ClassName: {} but NOT by name only".format(self.sa, A.sa))

if __name__ == "__main__":
    
    a = A()

    # in Python, class (effectively static) variable can be accessed through the class name or object name
    print(a.sa)
    print(A.sa)
