#students = 10
#capacity = 50

#f students < capacity:
#	print "Keep recruiting"
#else:
#	print "End ticket signups"


#teaching_assistants = 3

#if teaching_assistants == 0: #use two equal signs to compare, one to define a variable like students = 10
#	print "None? Uh-oh!"
#elif teaching_assistants < students/5:
#	print "Keep recruiting TAs"
#else:
#	print "Aren't the TAs great though?"
# != not equal to
# == equal to
# > greater than
# < less than
# >= greater than or equal to
# <= less than or equal to
# * multiplication
# / division


volunteers = 120
goal = 100

if volunteers == 0:
	print "You have no volunteers yet. Keep going to reach your goal of {0}!".format(goal)
elif volunteers == goal:
	print "Goal met! :)"
elif volunteers > goal:
	print "Ahead of goal by {0}!".format(volunteers-goal)
else:
	print "Behind goal by {0} :(".format(goal-volunteers)


gender = "F"

if gender == "f":
	print "Gender is female lowercase" 
	#this doesn't work because of the difference in case

if gender.lower() == "f":
	print "The gender is female"


print "55.0 / 2 is ", 55.0 / 2
print "55 / 2.0 is ", 55 / 2.0
print "55.0 / 2.0 is ", 55.0 / 2.0

