from datetime import date
from datetime import time
from datetime import datetime

def main():
	# Date Objects
	# get today's date
	today = date.today()
	print("Today's date is " + str(today))

	# get individual components of today's date
	print("Date Components: " + str(today.day) + " " + str(today.month) + " " + str(today.year))

	# retrieve today's weekday (0 = Monday, 6 = Sunday)
	print("Today's weekday #: " + str(today.weekday()))



	# Datetime Objects
	# get today's date using datetime
	today = datetime.now()
	print("The current datetime is " + str(today))

	d = datetime.date(today)
	print("The current date is " + str(d)) 

	# get the current time
	t = datetime.time(today)
	print("The current time is " + str(t))

	# get the current weekday
	w = date.weekday(today)
	days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
	print("The current weekday is " + str(days[w]))



	# Formatting
	now = datetime.now()
	print("%Y: " + now.strftime("%Y"))
	print("%a, %d, %B, %y: " + now.strftime("%a, %d, %B, %y"))
	print("local formatting %c: " + now.strftime("%c"))
	print("local formatted date %x: " + now.strftime("%x"))
	print("local formatted time %X: " + now.strftime("%X"))
	print("%I:%M:%S %p: " + now.strftime("%I:%M:%S %p"))
	print("%H:%M: " + now.strftime("%H:%M"))



	# Timedeltas
	from datetime import timedelta
	print("timedelta: " + str(timedelta(days=365, hours=5, minutes=1)))
	print("one year from now it will be: " + str(datetime.now() + timedelta(days=365)))
	print("two weeks and 3 days it will be: " + str(datetime.now() + timedelta(weeks=2, days=3)))
	t = datetime.now() - timedelta(weeks=1)
	s = t.strftime("%A %B %d, %Y")
	print("one week ago it was: " + s)
	# how many days until april fool's day
	today = date.today()
	afd = date(today.year, 4, 1)
	if afd < today:
		print("April Fool's Day already went by %d days ago" %(today-afd).days)	 
		afd = date(afd.year+1, 4, 1)
	time_to_afd = afd - today
	print("next April Fool's Day is %d days away" %time_to_afd.days)



	# Calendars
	import calendar
	c = calendar.TextCalendar(calendar.SUNDAY)
	str1 = c.formatmonth(2016, 11, 0, 0)
	print(str1)
	hc = calendar.HTMLCalendar(calendar.SUNDAY)
	str1 = hc.formatmonth(2016, 11)
	print(str1)
	for i in c.itermonthdays(2013, 8):
		print(i)
	# print out the first Friday of every month
	for m in range(1,13):
		cal = calendar.monthcalendar(2013,m)
		weekone = cal[0]
		weektwo = cal[1]

		if weekone[calendar.FRIDAY] != 0:
			meetday = weekone[calendar.FRIDAY]
		else:
			meetday = weektwo[calendar.FRIDAY]

		print("%10s %2d" %(calendar.month_name[m], meetday))



if __name__ == "__main__":
	main()