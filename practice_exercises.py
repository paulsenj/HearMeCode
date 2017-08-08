# <! Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

# numbers = range(2000,3201)
# answer = []
# for number in numbers:
# 	if number % 7 == 0 and number % 5 != 0:
# 		answer.extend([number])
# print answer

# <! Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

# print "What is your name?"
# name = raw_input()
# print "How old are you?"
# age = int(raw_input())
# # another option, this waits on the same line for input:
# # age = int(raw_input("How old are you?"))
# print "Pick a number from 1-5"
# pickanumber = int(raw_input())

# # this will print them all on one line, and is faster: 
# # print pickanumber * "You will turn 100 years old in {0}.".format(2016 - age + 100)

# numbers = range(0, pickanumber)
# for number in numbers:
# 	print "You will turn 100 years old in {0}.".format(2016 - age + 100)

# <! Take a list, say for example this one:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.

# test = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# result = []
# for number in test:
# 	if number < 5:
# 		result.append(number) #add this line to add them to a list
# print result

# <! Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 

# data = 253
# print "Let's find out the divisors of {}".format(data)
# data_points = range (1, data + 1)
# for x in data_points:
# 	if data % x == 0:
# 		print x

# <! Take two lists, and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). 
# Make sure your program works on two lists of different sizes. say for example these two:

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# c = []

# for x in a:
# 	if x not in c:
# 		if x in b:
# 			c.append(x)
# print c
			
# <! Ask the user for a string and print out whether this string is a palindrome or not. 
# (A palindrome is a string that reads the same forwards and backwards.)


# print "Think you know a palindrome? Enter it here!"
# string = raw_input()
# stringstrip = string.replace(" ", "").lower()
# print stringstrip
# backwards = stringstrip[::-1]
# print backwards

# if stringstrip == backwards:
# 	print "You found a palindrome! {} is the same forwards and backwards!".format(string.capitalize())


# <! Lets say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. 
# Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.

# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# b = []
# print a
# for x in a:
# 	if x % 2 == 0:
# 		b.append(x)
# print b

# c = [x for x in a if x % 2 == 0]
# print c

# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input),
# compare them, print out a message of congratulations to the winner,
# and ask if the players want to start a new game)

# print "Player 1, what do you choose? Rock, Paper, or Scissors?"
# player_1 = raw_input().lower()
# print "Player 2, what do you choose? Rock, Paper, or Scissors?"
# player_2 = raw_input().lower()

# options = ["rock", "paper", "scissors"]

# if player_1 in options and player_2 in options:
# 	if player_1 == "rock" and player_2 == "paper":
# 		print "Congratulations Player 2! Paper beats rock."
# 	elif player_1 == "rock" and player_2 == "scissors":
# 		print "Congratulations Player 1! Rock beats scissors."
# 	elif player_1 == "rock" and player_2 == "rock":
# 		print "It's a tie. Try again!"
# 	elif player_1 == "paper" and player_2 == "rock":
# 		print "Congratulations Player 1! Paper beats rock."
# 	elif player_1 == "paper" and player_2 == "scissors":
# 		print "Congratulations Player 2! Scissors beats paper."
# 	elif player_1 == "paper" and player_2 == "paper":
# 		print "It's a tie. Try again!"
# 	elif player_1 == "scissors" and player_2 == "paper":
# 		print "Congratulations Player 2! Scissors beats paper."
# 	elif player_1 == "scissors" and player_2 == "rock":
# 		print "Congratulations Player 1! Rock beats scissors."
# 	elif player_1 == "scissors" and player_2 == "scissors":
# 		print "It's a tie. Try again!"
# else: 
# 	print "One of you picked something that wasn't rock, paper, or scissors. Try again!"

import random
number = random.randint(1, 9)
print "Pick a number, any number (from 1 to 9)!"
guess = raw_input(int())

while guess != number:
	print "Guess again"
else:
		if guess < number:
			print "Higher! Guess again?"
			guess = raw_input(int())
		elif guess > number:
			print "Lower! Guess again?"
			guess = raw_input(int())



