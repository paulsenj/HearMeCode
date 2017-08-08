with open("states.csv", "r") as states_file:
	states = states_file.read().split("\n")

for index, state in enumerate(states):
	states[index] = state.split(",")

state_abbv = []

for state in states:
	state_abbv.append(state[0])

print state_abbv

state_name = []

for state in states:
	state_name.append(state[1])

print state_name


abbrv = []
names = []


#refers to an alternative option Ally showed
for index, state in enumerate(states):
	#new_state = state.split(',')
	states[index] = state.split(",")
	abbrv.append(states[index][0])
	# abbrv.append(new_state[0])
	names.append(states[index][1])

print abbrv
print names