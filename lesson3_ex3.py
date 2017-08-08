contacts = {
    "Hear Me Code": {
        "twitter": "@hearmecode",
        "github": "https://github.com/hearmecode"
    },
    "Shannon Turner": {
        "twitter": "@svt827",
        "github": "https://github.com/shannonturner"
    },
}

# How to add a new item to an existing dictionary:
contacts["Aliya Rahman"] = {
    "twitter": "@AliyaRahman",
    "github": "https://github.com/aliyarahman"
}

# Exercise 1: Add a new dictionary item to contacts for each person at your table.
#   Rather than editing lines 1-10 above, add new entries to the contacts dictionary below.
#   Keep in mind some people may not have a twitter account, and that's okay!

contacts["Jamie Paulsen"] = {
    "twitter":"@JamiePaulsen",
    "github": "https://github.com/paulsenj"
}

#print contacts

# Exercise 2: Loop through the contacts dictionary to display everyone's contact information.
#   Your output should look like this:

# Hear Me Code's info: 
#     twitter: @hearmecode
#     github: https://github.com/hearmecode
# Shannon Turner's info: 
#     twitter: @svt827
#     github: https://github.com/shannonturner


for item in contacts.items():
    name = item[0]
    twitter = item[1]["twitter"]
    github = item[1]["github"]
    print "{0}'s info:".format(name)
    print "\t twitter: {}".format(twitter)
    print "\t github: {}".format(github)



