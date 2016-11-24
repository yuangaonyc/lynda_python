# hello world
def main():
	print("hello world!")
# if __name__ == "__main__":
# 	main()




# variables
f = 0
# print(f)
f = 'abc'
# print(f)
# print('string type ' + str(123))

# global vs. local variable
def someFunction():
	global f
	f = 'def'
someFunction()
# print(f)

# deleting a variable
del f
# print(f) : this throws an error




# functions
def func1():
	print('I am a function')
# func1()
# print(func1())
# print(func1)

def func2(arg1, arg2):
	print(arg1,' ',arg2)
# func2(1, 2)
# print(func2(10,20))

def cube(x):
	return x*x*x
# print(cube(3))

def power(num, x=1):
	result = 1;
	for i in range(x):
		result = result * num
	return result
# print(power(2))
# print(power(2,3))
# print(power(x=3, num=2))

def multi_add(*args):
	result = 0;
	for x in args:
		result = result + x
	return result
# print(multi_add(4,5,10,4))
# print(multi_add(4,5,10,4,100))




# conditional structures
def main():
	x, y = 10, 100

	# if x < y :
	# 	st = 'x is less than y'
	# elif x == y :
	# 	st = 'x is equal to y'
	# else:
	# 	st = 'x is greater than y'
	
	st = 'x is less than y' if (x<y) else 'x is greater than or equal to y'
	print st

# if __name__=="__main__":
# 	main()




# loops
def whileloop():
	x = 0
	while x < 5:
		print(x)
		x += 1
# whileloop()

def forloop():
	for x in range(5,10):
		print(x)
# forloop()

days = ['Mon', 'Tue', 'Wen', 'Thu', 'Fri', 'Sat', 'Sun']
# for d in days:
# 	print(d)

for x in range(5,10):
	if (x == 7): break
	# print(x)

for x in range(5,10):
	if (x % 2 == 0): continue
	# print(x)

# for i, d in enumerate(days):
	# print(i, d) 




# classes
class myClass():
	def method1(self):
		print("myClass method1")

	def method2(self, someString):
		print("myClass method2: " + someString)

class anotherClass(myClass):
	def method2(self):
		print("anotherClass method2")

	def method1(self):
		myClass.method1(self)
		print("anotherClass method1")

def main():
	c = myClass()
	c.method1()
	c.method2("This is a string")
	c2 = anotherClass()
	c2.method1()
	c2.method2()

if __name__ == "__main__":
	main()











