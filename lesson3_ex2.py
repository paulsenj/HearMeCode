schools = {
    "geometry": {
        "coordinates": [
            -81.50572799999999, 
            39.21675500000001
        ]}, 
        "type": "Point"
    , 
    "properties": {
        "address": "300 Campus Drive, Parkersburg, WV 26104", 
        "marker-color": "#3F3040", 
        "marker-symbol": "circle", 
        "name": "West Virginia University at Parkersburg"
    }, 
    "type": "Feature"
}

# Example Question: How could you "slice" the dictionary to print "Feature" from line 15?

#print schools["type"]

#print schools.get("type")

# Question 1: What slice will give you a dictionary 
#   with the key of "coordinates" and a value containing a list
#   of two decimal numbers?

print schools.get("geometry")
print schools["geometry"]
print schools.get("geometry").get("coordinates")

# Question 2: What slice will give you the address of the school?

print schools.get("properties").get("address")

# Question 3: What slice will give you the name of the school?

print schools.get("properties").get("name")

# Question 4: What slice will give you the latitude of the school? 
#   (Hint: the latitude is 39.216...)

print schools.get("geometry").get("coordinates")[1]

# Question 5 (bonus): What slice will give you the marker-color 
#   without the hashtag in front?

print schools.get("properties").get("marker-color")[1:]