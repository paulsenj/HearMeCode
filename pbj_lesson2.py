# Difficulty level: Beginner

# Goal #1: Write a new version of the PB&J program that uses a while loop.  Print "Making sandwich #" and the number of the sandwich until you are out of bread, peanut butter, or jelly.

# Example:
# bread = 4
# peanut_butter = 3
# jelly = 10

# numberofsandwiches = min(bread/2, peanut_butter, jelly)

# while numberofsandwiches >=1:
	
# 	sandwiches = range(1, numberofsandwiches+1)
# 	for sandwich in sandwiches:
#  		print "Making sandwich #{}".format(sandwich)
# 		numberofsandwiches = numberofsandwiches - 1
# if numberofsandwiches == 0:
# 	print "All done; only had enough bread for {} sandwiches.".format(min(bread/2, peanut_butter, jelly))

# Output:
# Making sandwich #1
# Making sandwich #2
# All done; only had enough bread for 2 sandwiches.

# Goal #2: Modify that program to say how many sandwiches-worth of each ingredient remains.

# Example 2:
bread = 10
peanut_butter = 10
jelly = 4

numberofsandwiches = min(bread/2, peanut_butter, jelly)

while numberofsandwiches >= 1:
	sandwiches = range(1, numberofsandwiches+1)
	for sandwich in sandwiches:
 		print "Making sandwich #{}".format(sandwich)
		numberofsandwiches = numberofsandwiches - 1
		bread = bread - 2
		peanut_butter = peanut_butter - 1
		jelly = jelly - 1
		if numberofsandwiches >= 1:
			print "I have enough bread for {0} more sandwiches, enough peanut butter for {1} more, and enough jelly for {2} more.".format(bread/2, peanut_butter, jelly)
if jelly == 0:
	print "All done; I ran out of jelly."
if bread <= 1:
	print "All done; I ran out of bread."
if peanut_butter == 0:
	print "All done; I ran out of peanut butter."

# Output:
# Making sandwich #1
# I have enough bread for 4 more sandwiches, enough peanut butter for 9 more, and enough jelly for 3 more.
# Making sandwich #2
# I have enough bread for 3 more sandwiches, enough peanut butter for 8 more, and enough jelly for 2 more.
# Making sandwich #3
# I have enough bread for 2 more sandwiches, enough peanut butter for 7 more, and enough jelly for 1 more.
# Making sandwich #4
# All done; I ran out of jelly.