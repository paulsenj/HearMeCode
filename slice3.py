#Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

#Remember the rules: Rock beats scissors Scissors beats paper Paper beats rock
  
def rockpaperscissors():
  options = ["rock","paper","scissors"]
  player1 = raw_input("Player 1, what do you choose? Rock, paper, or scissors?").lower()
  player2 = raw_input("Player 2, what do you choose? Rock, paper, or scissors?").lower()
  if player1 in options and player2 in options:

	  while player1 == "rock":
	    if player2 == "paper":
	      print "Player 2 wins! Paper beats rock."
	      break
	    elif player2 == "scissors":
	      print "Player 1 wins! Rock beats scissors."
	      break
	    elif player2 == "rock":
	      print "Try again. You both chose rock."
	      break

	  while player1 == "paper":
	    if player2 == "rock":
	      print "Player 1 wins! Paper beats rock."
	      break
	    elif player2 == "scissors":
	      print "Player 2 wins! Scissors beats paper."
	      break
	    elif player2 == "paper":
	      print "Try again. You both chose paper."
	      break

	  while player1 == "scissors":
	    if player2 == "rock":
	      print "Player 2 wins! Rock beats scissors."
	      break
	    elif player2 == "paper":
	      print "Player 1 wins! Scissors beats paper."
	      break
	    elif player2 == "scissors":
	      print "Try again. You both chose scissors."
	      break
  else:
  	print "Someone chose something other than rock, paper, or scissors. Try again!"
#to play for the first time    
play = raw_input("Would you like to play Rock-Paper-Scissors? y/n").lower()
while play == "y":
  rockpaperscissors()
  play = raw_input("Would you like to play again? y/n").lower()
else:
  print "Ok, come back another time."

  
