#!/usr/local/bin/python3

class Person:
	
	def __init__(self, name):	
		self.name = name		

	def say_hi(self):
		print("hello from " + self.name)
		
p = Person("Frank")
print(p)
p.say_hi()
