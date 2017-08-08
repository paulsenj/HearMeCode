NW = []
NE = []
SW = []
SE = []

# [x] don't forget about 123 SEA LANE
# [x} don't forget about lower/upper case
#what if it's an entirely different city?
#what if they type out northwest?

#address = raw_input()
#print "What is your address?"

#if you added multiple addresses, you could split on new lines instead of spaces

for number in range(2): #this is running the whole code twice

	address = "456 fake st nw Washington, DC 20036".upper()
	#if we turn this address into a list, it'll break out each piece instead of searching within the whole thing
	#address = address.split(" ") 
	print address
	if "NW" in address.split(" "):
		NW.append(address)
		print "It is in NW"
	elif "NE" in address.split(" "):
		NE.append(address)
		print "It is in NE"
	elif "SW" in address.split(" "):
		SW.append(address)
		print "It is in SW"
	elif "SE" in address.split(" "):
		SE.append(address)
		print "It is in SE"
	else: #else catches everything else that's not already been captured
		print "Not in DC or no quadrant"
	print "We have {} address in NW. The address is {}.".format(len(NW), NW)
	print "We have {} address in NE. The address is {}.".format(len(NE), NE)
	print "We have {} address in SW. The address is {}.".format(len(SW), SW)
	print "We have {} address in SE. The address is {}.".format(len(SE), SE)
