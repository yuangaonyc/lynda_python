# when re-assign value to a variable, the id changes
x = 42
print(x)
print(id(x))
print(type(x))
x = 43
print(x)
print(id(x))
print(type(x))
x = 42
print(x)
print(id(x))
print(type(x))
print(" ")

# int and float
num = 42 
print(type(num), num)
div = 42 / 9
print(type(div), div)
div2 = 42 // 9
print(type(div2), div2)
num = 42.0
print(type(num), num)
print(" ")

# string
s = "This is a \nstring"
print(s)
s = r"This is a \nstring"
print(s)
n = 42
s = "This is a {} string".format(n)
print(s)
n = 42 
s = '''\
this is a string \
line after line 
of text and more
text.
	'''
print(s)

# list and tuple
x = (1, 2, 3)
print(type(x), x)
x = [1, 2, 3]
print(type(x), x)
x.insert(2, 7)
print(type(x), x)
x = 'string'
print(type(x), x[2:4])
for i in x: print(type(i), i)
print(" ")

# dictionary
d = {'one': 1,
	 'two': 2,
	 'three': 3,
	 'four': 4,
	 'five': 5
	}
for k in sorted(d.keys()):
	print(k, d[k])
d = dict(
	one = 1, 
	two = 2,
	three = 3,
	four = 4,
	five = 'five'
	)
for k in sorted(d.keys()):
	print(k, d[k])
print(" ")

# identifying an object
x = 42
print(x)
print(id(x))
print(type(x))
print(id(42))
print(type(42))
y = 42
print(x == y) # compares value
print(x is y) # compares id
x = dict( x = 42 )
print(type(x))
print(x)
print(id(x))
y = dict( x = 42 )
print(type(y))
print(y)
print(id(y))
print(x == y) # same value
print(x is y) # diff objects
print(" ")

# True and False objects
a, b = 0, 1
print(a == b)
print(a < b)
print(a > b)
a = True
print(type(a))
print(id(a))
b = True
print(type(b))
print(id(b))
print(id(True))




























