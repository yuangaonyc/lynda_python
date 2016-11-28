# If elif and else
diet_restrictions = set(['meat', 'cheese'])

if 'meat' in diet_restrictions:
	print('Get a cheese pizza.')
elif 'meat' and 'cheese' in diet_restrictions:
	print('Get a vegan pizza.')
else:
	print('Get something else.')

if 'meat' and 'cheese' in diet_restrictions:
	print('Get a vegan pizza.')
elif 'meat' in diet_restrictions:
	print('Get a cheese pizza.')
else:
	print('Get something else.')

# Dictionarize an if-elif chain to make it faster
today = 'Saturday'

if today is 'Sunday':
	print('Order the spinach pizza.')
elif today is 'Monday':
	print('Order the mushroom pizza.')
elif today is 'Tuesday':
	print('Order the pepperoni pizza.')
elif today is 'Wednesday':
	print('Order the veggie pizza.')
elif today is 'Thursday':
	print('Order the chicken pizza.')
elif today is 'Friday':
	print('Order the sausage pizza.')			
elif today is 'Saturday':
	print('Order the Hawaiian pizza.')

specials = {'Sunday' : 'spinach',
			'Monday' : 'mushroom',
			'Tuesday' : 'pepperoni',
			'Wednesday' : 'veggie',
			'Thursday' : 'bbq chicken',
			'Friday' : 'sausage',
			'Saturday': 'Hawaiian'}
def order(day):
	pizza = specials[day]
	print('Order the {} pizza'.format(pizza))
order(today)
print(" ")




# For loops
sink = ['bowl', 'plate', 'cup']

for dish in list(sink):
	print('Putting {} in the dishwasher'.format(dish))
	sink.remove(dish)
















