# trying to download things that dont exist
import urllib.request
try:
	webpage = urllib.request.urlopen('http://www.fakegoogle.com')
except:
	print('Could not access webpage!')
else:
	for line in webpage:
		print(line)

# overloading a circuit breaker
class CircuitBreaker:
	def __init__(self, max_amps):
		self.capacity = max_amps
		self.load = 0

# 	def connect(self, amps):
# 		if self.load + amps > self.capacity:
# 			raise Exception('connect will exceed capacity')
# 		elif self.load + amps < 0:
# 			raise Exception('connect will cause negative load')
# 		else:
# 			self.load += amps

# cb = CircuitBreaker(20)
# print(cb.load)
# cb.connect(12)
# cb.connect(7)
# cb.connect(10)
# print(cb.load)

# creating custom errors
class ElectricalError(Exception): # inherit from Exception class

	def __init__(self, device, problem):
		self.device = device
		self.problem = problem

	def __str__(self):
		return "The {} is {}!".format(self.device, self.problem)

class PlumbingError(Exception):

	def __init__(self, device, problem):
		self.device = device
		self.problem = problem

	def __str__(self):
		return "The {} is {}!".format(self.device, self.problem)

def cause_error(error_type):

	if error_type == 'electrical':
		raise ElectricalError('cicuit breaker', 'overloaded')

	elif error_type == 'plumbing':
		raise PlumbingError('dishwasher', 'spraying water')

	else:
		raise Exception('a generic household problem')

try:
	cause_error('electrical')
except ElectricalError as e:
	print(e)
	print('Fix it myself.')
except PlumbingError as e:
	print(e)
	print('Call the plumber.')
except:
	print('Call the landlord.')

try:
	cause_error('plumbing')
except ElectricalError as e:
	print(e)
	print('Fix it myself.')
except PlumbingError as e:
	print(e)
	print('Call the plumber.')
except:
	print('Call the landlord.')

try:
	cause_error('grass')
except ElectricalError as e:
	print(e)
	print('Fix it myself.')
except PlumbingError as e:
	print(e)
	print('Call the plumber.')
except:
	print('Call the landlord.')
print(" ")




# Polling
import time
hungry = True;

while(hungry):

	print('Opening the front door')
	front_door = open('front_door.txt', 'r')

	if "Pizza Guy" in front_door:
		print("Pizza's here!")
		hungry = False
	else:
		print("Not yet...")

	print('CLosing the front door.')
	front_door.close()

	time.sleep(1)

# Handling events
import tkinter
import time

def alarm(): # envet handlers
	print('Calling the Pizza Company')

def doorbell():
	print('Ding Dong!')
	time.sleep(4)
	print('Opening the Door')

def phonecall():
	print('Answering the phone.')

root = tkinter.Tk() # create buttons and assign callbacks
tkinter.Button(root, text='Ring Doorbell', command=doorbell).pack()
tkinter.Button(root, text='Call Phone', command=phonecall).pack()

root.after(8000, alarm) # timer event

root.mainloop()




