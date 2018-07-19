#!/usr/bin/env python3

while True:
    try:
        x = int(input("Please enter a number: "))
    except ValueError:
        print("Oops! That was not a valid number.")
