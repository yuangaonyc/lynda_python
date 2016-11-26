# Objects
def main():
	print("shirt")
	print(type("shirt"))
	print(dir("shirt"))
	print("shirt".upper())
	print(id("shirt"))
	print(id("pants"))
	print(id(1))
	print(dir(1))
	print(" ")

if __name__ == "__main__":
	main()

class shirt:

	def __init__(self):
		self.clean = True

	def make_dirty(self):
		self.clean = False

	def make_clean(self):
		self.clean = True

def main():
	red = shirt()
	crimson = red
	print(id(red))
	print(id(crimson))
	print(red.clean)
	print(crimson.clean)
	red.make_dirty()
	print(red.clean)
	print(crimson.clean)
	print(red is crimson)
	crimson = shirt()
	print(red is crimson)

	print(" ")

if __name__ == "__main__":
	main()

def main():
	closet = ['shirt', 'hat', 'pants', 'jacket', 'socks']
	print(id(closet))
	print(closet)
	closet.remove('hat')
	print(id(closet))
	print(closet)
	words = "You're wearing that"
	print(id(words))
	print(words)
	words = words + " because you look great!"
	print(id(words))
	print(words)

	print(" ")

if __name__ == "__main__":
	main()










# Class Inheritance
class Vehicle: # base vehicle class
	
	def __init__(self, color, manuf):
		self.color = color
		self.manuf = manuf
		self.gas = 4 # a full tank of gas

	def drive(self):
		if self.gas > 0:
			self.gas -= 1
			print("The {} {} goes VROOM!".format(self.color, self.manuf))
		else:
			print("The {} {} sputters out of gas".format(self.color, self.manuf))

class Car(Vehicle): # inherits from vehicle class

	def radio(self): # turn the radio on
		print("Rockin Tunes!")

	def window(self): # open the window
		print("Ahhh... fresh air!")

class Motorcycle(Vehicle): # Inherits from vehicle class
	
	def helmet(self): # put on motocycle helmet
		print("Nice and safe")

class ECar(Car): # inherits from car class
	
	def drive(self):
		print("The {} {} goes ssshhhhh!".format(self.color, self.manuf))


def main():
	my_car = Car("red", "Mercedes")
	my_mc = Motorcycle("silver", "Harley")
	my_car.drive()
	my_car.drive()
	my_car.drive()
	my_car.drive()
	my_car.drive()
	my_mc.drive()
	my_car.radio()
	my_car.window()
	my_mc.helmet()
	my_ecar = ECar("white", "Nissan")
	my_ecar.window()
	my_ecar.radio()
	my_ecar.drive()
	print(my_ecar.gas)
	print(" ")

if __name__ == "__main__":
	main()










# Modules and Packages

def main():
	import random
	print(random.randint(1,20))
	# print(randint(1,20)) this would give an error
	from random import randint
	print(randint(1,20))
	import random as rand
	from random import random
	print(rand.randint(1,20))
	print(random())

	# packages(urllib) is a collection of modules(request)
	import urllib.request
	print(urllib.request.urlopen("http://www.google.com"))
	print(urllib.__path__)

if __name__ == "__main__":
	main()









