print("Hello, World!")
print(" ")

# conditionals
a, b = 5, 1
if a < b:
	print('a ({}) is less than b ({})'.format(a,b))
else:
	print('a ({}) is not less than b ({})'.format(a,b))
print("foo" if a < b else "bar")
print(" ")

# while loops
a, b = 0, 1
while b < 50:
	print(b)
	a, b = b, a+b
print("Done.")
print(" ")

# for loops
fh = open('lines.txt')
for line in fh.readlines():
	print(line, end='')
print("\n")

# functions
def isprime(n):
	if n == 1:
		print('1 is special')
		return False
	for x in range(2, n):
		if n % x == 0:
			print("{} equals {} * {}".format(n, x, n//x))
			return False
	print(n, "is a prime number")
	return True
for n in range(1, 20):
	isprime(n)
print(" ")

# generator function
def isprime(n):
	if n == 1:
		return False
	for x in range(2,n):
		if n % x == 0:
			return False
	else:
		return True
def primes(n = 1):
	while(True):
		if isprime(n): yield n
		n += 1
for n in primes():
	if n > 100: break
	print(n, end=" ")
print("\n")

# simple oop
class Fibonacci():
	def __init__(self, a, b):
		self.a = a
		self.b = b
	def series(self):
		while(True):
			yield(self.b)
			self.a, self.b = self.b, self.a +self.b
f = Fibonacci(0,1)
for r in f.series():
	if r > 100: break
	print(r, end=" ")
print("\n")

# oop2
class AnimalActions:
	def quack(self): return self.strings['quack']
	def feathers(self): return self.strings['feathers']
	def bark(self): return self.strings['bark']
	def fur(self): return self.strings['fur']
class Duck(AnimalActions):
	strings = dict(
		quack = "Quaaaak!",
		feathers = "The duck has grau and white feathers.",
		bark = "The duck cannot bark.",
		fur = "The duck has no fur."
		)
class Person(AnimalActions):
	strings = dict(
		quack = "The person imitates a duck.",
		feathers = "The person takes a feather from the ground and shows it.",
		bark = "The person syas woof!",
		fur = "The person puts on a fur coat"
		)
class Dog(AnimalActions):
	strings = dict(
		quack = "The dog cannot quack.",
		feathers = "The dog has no feathers",
		bark = "Arf!",
		fur = "The dog has white fur with black spots."
		)
def in_the_doghouse(dog):
	print(dog.bark())
	print(dog.fur())
def in_the_forest(duck):
	print(duck.quack())
	print(duck.feathers())
def main():
	donald = Duck()
	john = Person()
	fido = Dog()
	print("- In the forest:")
	for o in (donald, john, fido):
		in_the_forest(o)
	print("- In the doghouse:")
	for o in (donald, john, fido):
		in_the_doghouse(o)
if __name__ == "__main__":
	main()
	print(" ")

# exceptions
try:
	fh = open('xlines.txt')
	for line in fh.readlines():
		print(line)
except IOError as e:
	print("something bad happened ({})".format(e))
print("after badness")













