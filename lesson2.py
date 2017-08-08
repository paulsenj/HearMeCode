#the keyboard shortcut COMMAND SLASH will turn whatever you've highlighted into a comment

attendees = ['Shannon', 'Jenn', 'Grace']
#print attendees
#print len(attendees) #3 - this counts the number of items in a list or how many characters in a string
#print attendees[0] # Shannon
#print attendees[1] # Jenn
#print attendees[2] # Grace
#print attendees[0:2] # Shannon, Jenn as ['Shannon', 'Jenn']
#print attendees[3] gives error "IndexError: List index out of range"
#print attendees[0:3]
#number_of_attendees = len(attendees) #save answer as a variable
#print number_of_attendees
#print "If we need one TA for every 3 students, we currently need {} TA(s).".format(number_of_attendees/3)

# list.append() adds an item to the end
# attendees_ages = []
# attendees_ages.append(28)
# print attendees_ages #28
# attendees_ages.append(27)
# print attendees_ages # [28, 27]
# attendees_ages[0] = 29 #replace the value for the specific piece of the list
# print attendees_ages # [29, 27]

days = ["Monday", "Tuesday"]
print days
days.append("Wednesday")
#print days #Monday, Tuesday, Wednesday
#print "There are this many days in the week: {}".format(len(days))
days.append("Thursday")
#print days
days.append("Friday")
#print days
days.append("Saturday")
#print days
days.append ("Sunday")
#print days
#print len(days)
days_in_the_week = len(days)
# print "Just kidding. There are actually {} days in the week.".format(days_in_the_week)
# print "The first day of the week is {}.".format(days[0])
# print "The last day of the week is {}.".format(days[6])
#.pop removes one item from the end of the list
# day = days.pop() #remove Sunday
# print day #the item being removed
# print days #the list now that we've removed one item
# day = days.pop(3) #remove a specific item from the list by slicing number, but saved as a variable
# print day 
print days

#using the for loop to print each item
for day in days:
	print day

# months = ["January", "February"]
# print months
# months.extend(["March", "April", "May", "June", "July", "August", "September", "November", "December"])
# #.extend adds many. Need brackets inside the parentheses, because it's a lists
# print months
# #remove December
# months.pop()
# print months
# #add it back in
# months.append("December")
# print months
# #remove January
# months.pop(0)
# print months
# #add it back in. Insert "January" BEFORE index 0
# months.insert(0, "January")
# print months
# # months.insert("February",1) Error: TypeError: an integer is required
# # months.insert(3, March) Error: name "March" is not defined

# address = "1133 19th St NW Washington, DC 20036"
# print address
# #turn it into a list based on the character you determine, in this case a space " "
# address_as_list = address.split(" ")
# print address_as_list

# #the "in" keyword allows you to check whether a value exists in the list OR string
# print "ann" in "Shannon" #True
# print "Frankenstein" in attendees #False
# print "Shannon" in attendees #True

# #Come back and try to make this work later!
if ("Shannon" in attendees) is True:
 	print "Shannon is attending."

# Shannon_coming = "Shannon" in attendees
# if Shannon_coming == True:
# 	print "Shannon's coming!"















