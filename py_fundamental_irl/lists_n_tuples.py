# Lists and Tuples

row = ['Ford', 'Audi', 'BMW', 'Lexus']
row.append('Mercedes')
print(row)
print(row[4])
row[2] = 'Jeep'
print(row)
print(row[4])
row.append('Honda')
print(row)
print(row[4])
row.insert(0, 'Kia')
print(row[4])
print(row.index('Mercedes'))
print(row.pop(5))
print(row)
row.remove('Lexus')
print(row)
print(" ")

# Multi-dimonsional Lists
# 2D list of lists
# - index cars by row, spot
lot_2d = [
		  ['Toyota', 'Audi', 'BMW'], # 0th row
		  ['Lexus', 'Jeep'],		 # 1st row
		  ['Honda', 'Kia', 'Mazda']	 # 2nd row
		  ]

# 3D list of lists of lists
# - index cars by floor, row, spot
lot_3d = [[								# 0th floor
		   ['Telsa', 'Fiat', 'BMW'], 
		   ['Honda', 'Jeep'],
		   ['Saab', 'Kia', 'Ford']
		  ],
		  [								# 1st floor
		   ['Subaru', 'Nissan'],
		   ['Volvo']
		  ],
		  [								# 2nd floor
		   ['Mazda', 'Chevy'],
		   [],
		   ['Volkswagen']
		  ]
		 ]

print(lot_2d[2])
print(lot_2d[2][1])
print(lot_3d[0])
print(lot_3d[0][2])
print(lot_3d[0][2][1])
print(" ")

for floor in lot_3d:
	for row in floor:
		for car in row:
			print(car)
print(" ")
		
# Tuples
my_tuple = ('a','b','c',1,2,3)
print(my_tuple[2])
# my_tuple[2] = 3 this gives an error

# Where's My Mouse?
import tkinter

def mouse_click(event):

	#retrieve XY coords as a tuple
	coords = root.winfo_pointerxy()
	print('coords: {}'.format(coords))
	print('X: {}'.format(coords[0]))
	print('Y: {}'.format(coords[1]))

root = tkinter.Tk()
root.bind('<Button>', mouse_click)
root.mainloop()






