#key always has to be a string, value can be anything (list, dictionary, number)
#Shannon is key, #202-555-1234 is the value

#key must be unique
phonebook = {
	'Shannon': '202-555-1234',
	'Bridget': '202-555-5678'
}

print phonebook['Shannon']

print phonebook

phonebook['Mel'] = '301-555-2345'

print phonebook

#print phonebook['Frankenstein']
#this throws an error because it is not in the phonebook. Solving using .get below

print phonebook.get('Frankenstein')
print phonebook.get('Mel')
print phonebook.get('Frankenstein', "I couldn't find that name.")
#add a second value and that will replace "None" as the result if the value can't be found

phonebook_keys = phonebook.keys()
print phonebook_keys

for key in phonebook_keys:
	print key,
	print phonebook[key]

#dictionaries aren't ordered, but we can use the sorted function to sort

print sorted(phonebook_keys)

print phonebook
print phonebook.items()

for key, value in sorted(phonebook.items()):
	print key, value
