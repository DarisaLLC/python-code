#!/usr/bin/env python3

"""
decorators :
- a decorator adds extra functionality to a function
- decorators recieve an input function, wrap it in a decorated function which calls the input and perform other actions, and return the decorated function
- decorators can be stacked, meaning the output from the decorator underneath is passed to the decorator on top when Python processes the original function definition
- after all decorators are processed, the original function named is bound to the output from the topmost decorator
"""

def helloSolarSystem(input_function):
    def decorated_function(*args, **kwargs):
        input_function(*args, **kwargs)
        print("in decorator helloSolarSystem()...")
    return decorated_function

def helloGalaxy(input_function):
    def decorated_function(*args, **kwargs):
        input_function(*args, **kwargs)
        print("in decorator helloGalaxy()...")
    return decorated_function

@helloGalaxy
@helloSolarSystem
def hello(name=None):
    if name is None:
        print("hello world...")
    else:
        print("hello {}...".format(name))

if __name__ == "__main__":
    hello("jackson")
