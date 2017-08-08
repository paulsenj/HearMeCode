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

with open("state_abbrev2.txt", "w") as abbrev_file:
	abbrev_file.write(str(state_abbv))

#.join on a space is what makes it look nice when I export it