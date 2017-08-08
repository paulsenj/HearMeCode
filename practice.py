index = "S&P 500"
print index
print index.lower()
print index.find("&")
print "The Standard & Poor's index is abbreviated as {}.".format(index[0:3])
print "There are {} companies included in the index.".format(index[4:])
print "If we added 10 companies it would be the {} index.".format(index.replace("500","510"))
closing_price = 1999.99
fiftytwo_week_high = 2134.72

if closing_price < fiftytwo_week_high:
	print "The {} closed at {} today, off {} points from the 52 week high.".format(index, closing_price, -1*(closing_price - fiftytwo_week_high))
if closing_price == fiftytwo_week_high:
	print "In a shocking turn of events, the {} closed at {}, exactly matching its 52 week high.".format(index, closing_price)
if closing_price > fiftytwo_week_high:
	print "The {} made shocking gains today, closing at {}, up {} points from the 52 week high.".format(index, closing_price, (closing_price - fiftytwo_week_high))