#!/usr/local/bin/python3

class Robot:
	population = 0 # class variable 
	
	def __init__(self, name):
		self.name = name 
		print("Initializing {}".format(self.name))
		Robot.population += 1

	def die(self):
		print("{} is being destroyed".format(self.name))
		Robot.population -= 1
		
		if Robot.population == 0:
			print("{} was the last robot".format(self.name))
		else:
			print("there are still {:d} robots working".format(Robot.population))

	def say_hi(self):
		print("greetings human, my overlords call me {}".format(self.name))

	@classmethod
	def how_many(cls):
		print("we have {:d} robots".format(cls.population))

droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

print("robots peform work...")

print("destroying robots...")
droid1.die()
droid2.die()

