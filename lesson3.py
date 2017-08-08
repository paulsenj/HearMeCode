#If the file was stored on my desktop, use something like this 
#instead of just states.txt "/Users/elliot/Desktop/states.txt"

with open("states.txt", "r") as states_file:
	states = states_file.read().split("\n")

for index, state in enumerate(states):
	#print (index, state) prints 1 AL Alabama, 2 AK Alaska, etc.
	#print state.split('\t') prints ['AL', 'Alabama']
	states[index] = state.split("\t")
	#puts each list for each state within a bigger list

print states

state_name = []
for state in states:
	state_name.append(state[1])

print state_name

state_abbv = []
for state in states:
	state_abbv.append(state[0])

print state_abbv