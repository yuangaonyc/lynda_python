# Modules and Packages

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
print(" ")

