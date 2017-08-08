phone = "202-555-6789"
print "Call {0} for great pizza!".format(phone[4:])
print "Washington, DC's area code is {0}.".format(phone[0:3])
print "Call {0} {1} for great pizza!".format(phone[0:3], phone[4:])

tweet = """In just over one year, @hearmecode has reached over 800 members who are learning how to code together."""

print """That tweet is {0} characters.
You have {1} characters left.""".format(len(tweet), 140-len(tweet))