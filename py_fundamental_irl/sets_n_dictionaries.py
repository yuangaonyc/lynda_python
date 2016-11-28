# Sets
college = set(['Bill', 'Katy', 'Verne', 'Dillon',
			   'Bruce', 'Olivia', 'Richard', 'Jim'])
coworker = set(['Aaron', 'Bill', 'Brandon', 'David',
				'Frank', 'Connie', 'Kyle', 'Olivia'])
family = set(['Gary', 'Landon', 'Larry', 'Mark',
			  'Olivia', 'Katy', 'Rae', 'Tom'])

print(len(college))
print(len(coworker))
print(len(family))

friends = college.union(coworker, family)
print(friends)

# Sorting sets
zipcode = set(['Jerry', 'Elaine', 'Cindy', 'Verne',
			   'Rudolph', 'Bill', 'Olivia', 'Jim',
			   'Lindsay', 'Rae', 'Mark', 'Kramer',
			   'Landon', 'Newman', 'George'])
munchkins = set(['Steve', 'Jackson', 'Frank', 'Bill',
				 'Mark', 'Landon', 'Rae'])
olivia = set(['Jim', 'Amanda', 'Verne', 'Nestor'])

local = friends.intersection(zipcode)
print(local)
invite = local.difference(munchkins)
print(invite)
invite = invite.symmetric_difference(olivia)
print(invite)

# Add and remove items from sets
print('Verne' in invite)
invite.add('Verne')
print(invite)
invite.add('Olivia')
print(invite)
invite.remove('Nestor')
print(invite)
print(invite.pop())
print(invite.pop())
print(invite.pop())
print(" ")



# Dictionaries
rolodex = {'Aaron' : 5556069,
		   'Bill' : 5559824,
		   'Dad' : 5552603,
		   'David' : 5558331,
		   'Dillon' : 5553538,
		   'Jim' : 5555547,
		   'Mom' : 5552603,
		   'Olivia' : 5556397,
		   'Verne' : 5555309
		   }

print(rolodex['Verne'])
print(hash('Verne'))

rolodex['Amanda'] = 5559754
print(rolodex['Amanda'])
print(rolodex['David'])
rolodex['David'] = 5550902
print(rolodex['David'])
rolodex['David'] = (5558331, 5550902)
print(rolodex['David'])
rolodex['David'] = 5558331
rolodex['David (Amanda)'] = 5550902
print(rolodex['David'])
print(rolodex['David (Amanda)'])

def caller_id(lookup_number):
	for name, num in rolodex.items():
		if num == lookup_number:
			return name
print(caller_id(5556397))
print(caller_id(0000000))
print(caller_id(5552603))













