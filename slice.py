phone = "(202) 456-7890"
print phone
print phone[1:4]
print phone [6:9]
print phone [10:15]
print phone [0:5]
print phone [6:15]
print phone [-4:]
print phone [-8:]

name = "Jamie"
age = 29
print "My name is {0} and my age is {1}".format(name, age)

area_code = phone [0:5]
phone_number = phone [6:15]
print area_code

print "Washington DC's area code is {0}. Shannon's phone number is {1}.".format(area_code, phone_number)

position = phone.find("(")
print position