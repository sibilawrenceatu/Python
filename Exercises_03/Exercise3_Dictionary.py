#my dictionary 1 contents
my_dictionary1 = {"name":"Sibi","age":"55","job":"IT Professional"}
#printing my dictionary1 contents
print ("the contents of first dictionary is ",my_dictionary1)
#printing the name from the dictionary
print ("the dictionary item 'name' is " ,my_dictionary1["name"])
#Replacement of item "age" with "80" of dictionary
my_dictionary1["age"] = 80
print ("the contents of updated dictionary with Age 80 is ",my_dictionary1)
my_dictionary1["likes"] = "Cricket"
print ("the contents of updated dictionary with 'likes' field is ",my_dictionary1)
#printing my dictionary1 values alone
print ("all the current values in my_dictionary1 are - ", my_dictionary1.values())
#printing my dictionary1 keys alone
print ("all the current keys in my_dictionary1 are - ", my_dictionary1.keys())
#printing my dictionary1 all items
print ("all the items in my_dictionary1 are - ", my_dictionary1.items())
