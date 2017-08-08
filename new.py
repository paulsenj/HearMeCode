with open("states.csv", "r") as states_file:
	states = states_file.read().split("\n")

for state in states:
	states = state.split(",")

print states