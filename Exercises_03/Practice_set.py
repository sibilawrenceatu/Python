#Program for set functionalities
#Create a blank set
my_set = set()
#adding 9,10, and 11 integers to the set
my_set.add(11)
my_set.add(10)
my_set.add(9)
#Printing the values of current set
print ("my current set is ", my_set)
#Sets only contatin unique values. Adding a duplicate value 10 will not get added to the set. Adding another unique value 12 also to set
my_set.add(10)
my_set.add(12)
print ("my new set is ",my_set)