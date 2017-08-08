#most common: range from 0 to ...
# print range(5) #5 items long starting at 0
#range (start, stop)
# print range(5,10) # 5 items long starting at 5

#for loop is most common and most useful kind of loop. for every item in the list, print that single item
# for number in range(10):
	# print number

# #use this when you need to do a task a certain number of times
# attendees = ["Kira", "Jamie", "Mago", "Stacey", "Diana", "Tiffany", "Angel", "Michelle", "Sue Ellen", "Cheryl", "Carla", "Katie", "Mirabel", "Maria", "Maria", "Megan", "Heather", "Sarah", "Ariana"]
# print attendees

# #use a plural word for the list, like attendees, and then the singular for each
#enumerate gives the number first
#for index, name in enumerate(attendees):
#		print "I am {} and my number is {}".format(name, index)

# for name in attendees:
# 		print name

# print list(enumerate(attendees)) #prints (number, name) as sets within a list

# #same as saying:
# attendee = "Kira"
# print attendee
# attendee = "Jamie"
# print attendee
# attendee = "Mago"
# print attendee
# attendee = "Stacey"
# print attendee

# for week in range(1, 5):
# 	print "Week {}".format(week)

# #same as:
# for week in [1, 2, 3, 4]:
# 	print "Week {}".format(week)

# days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# #indendation is super important. This way would only give you each once:
# # for week in range(1, 5):
# # 	print "Week {}".format(week)

# # for day in days_of_week:
# # 	print day

# months_in_year = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
# for month in months_in_year:
# 	print month

# 	for week in range(1, 5):
# 		print "\t Week {}".format(week)

# 		for day in days_of_week:
# 			print day

# for month in months_in_year:
# 	for week in range(1, 5):
# 		for day in days_of_week:

# 			print "Month:{0} Week:{1} Day: {2}".format(month, week, day)

#ennumerate() is a function that we can use with a for loop to get the index(position) of that list item

# team_bluelabs = ["Tiffany", "Angel", "Michelle", "Sue Ellen"]
# team_marigolds = ["Maria", "Maria", "Megan", "Heather"]

# for bluelab, marigold in zip(team_bluelabs, team_marigolds):
# 	print bluelab, marigold
