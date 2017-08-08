email = "jamie.paulsen@gmail.com"
print email
print email.find("@")
#finds only the first instance
print "Your e-mail domain is {0}".format(email[14:])
print email.find("Z") #returns -1 when it doesn't find it
print email [0:13]

twitter = "@hearmecode"
print twitter.replace("@","#") 
#this replaces the character only for this run, but replaces every instance of this character
print twitter

#this changes the value of the variable permenantly from this point on
twitter = twitter.replace("@","#")
print twitter

print "This string has an @ symbol, but I want to change it to a # symbol".replace("@","#")

address = "          1600 Pennsylvania Avenue   "
print address
print address.strip()
#.strip removes spaces before and after the first and last characters, but not between

gender = "F"
print gender
print gender.lower()
print gender.upper()
#convert the whole string to lower or upper case
