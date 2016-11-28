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

