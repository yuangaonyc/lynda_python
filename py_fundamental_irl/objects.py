# Objects
print("shirt")
print(type("shirt"))
print(dir("shirt"))
print("shirt".upper())
print(id("shirt"))
print(id("pants"))
print(id(1))
print(dir(1))
print(" ")



class shirt:

	def __init__(self):
		self.clean = True

	def make_dirty(self):
		self.clean = False

	def make_clean(self):
		self.clean = True

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