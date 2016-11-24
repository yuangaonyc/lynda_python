# txt file o/c
def main():
	f = open("textfile.txt", "w+")
	for i in range(10):
		f.write("This is line %d\r\n" %(i+1))
	f.close()

	f = open("textfile.txt", "a+")
	for i in range(10, 20):
		f.write("This is line %d\r\n" %(i+1))
	f.close()

	f = open("textfile.txt", "r")
	if f.mode == 'r':
		contents = f.read()
		print(contents)
	f.close()

	f = open("textfile.txt", "r")
	if f.mode == 'r':
		fl = f.readlines()
		for line in fl:
			print(line)
	f.close()

if __name__ == "__main__":
	main()




# working with os.path module
import os 
from os import path
import datetime
from datetime import date, time, timedelta
import time

def main():
	# print the name of the os
	print(os.name)
	# check fo item existence and type
	print("Item exists: " + str(path.exists("textfile.txt")))
	print("Item is a file: " + str(path.isfile("textfile.txt")))
	print("Item is a directory: " + str(path.isdir("textfile.txt")))
	# work with file paths
	print("Item's path: " + str(path.realpath("textfile.txt")))
	print("Item's path and name: " + str(path.split(path.realpath("textfile.txt"))))
	# get the modification time
	t = path.getmtime("textfile.txt")
	print(t)
	print(time.ctime(t))
	print(datetime.datetime.fromtimestamp(t))
	# calculate how long ago the item was modified
	now = datetime.datetime.now()
	modi = datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
	print("The file was editted " + str((now-modi).total_seconds()) +" seconds ago")

if __name__ == "__main__":
	main()



# shell
import os
import shutil
from os import path
from shutil import make_archive
from zipfile import ZipFile

def main():
	if path.exists("textfile.txt"):
		src = path.realpath("textfile.txt")
		head, tail = path.split(src)
		print("path: " + head)
		print("file: " + tail)
		dst = src + ".bak"
		# shutil.copy(src, dst) (copies only content)
		# shutil.copystat(src, dst) (copies meta data too)
		# os.rename("textfile.txt", "newfile.txt")
		# root_dir, tail = path.split(src)
		# shutil.make_archive("archive", "zip", root_dir)
		with ZipFile("testzip.zip", "w") as newzip:
			newzip.write("textfile.txt")

if __name__ == "__main__":
	main()












