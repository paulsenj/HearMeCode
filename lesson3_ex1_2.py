with open("states.csv", "r") as states_file:
	states = states_file.read().split("\n")

for index, state in enumerate(states):
	states[index] = state.split(",")

state_abbv = []

for state in states:
	state_abbv.append(state[0])

#print state_abbv

state_name = []

for state in states:
	state_name.append(state[1])

#print state_name

with open("state_abbrev.txt", "w") as abbrev_file:
	abbrev_file.write(", ".join(state_abbv))

#.join on a space and a comma is what makes it look nice when I export it

with open("state_longname.txt", "w") as abbrev_file:
	abbrev_file.write(", ".join(state_name))