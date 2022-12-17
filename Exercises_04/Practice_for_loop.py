#Program to check the for loop functionalities
#my_list containing digits 1-10
my_list = [1,2,3,4,5,6,7,8,9,10]
#for loop iterate through the list of items
for item in my_list:
#each item in list is checked with modulus function and print its value if modulus is not equal to 0
 if item %2 != 0:
  print(item,end = " ")
print ("\n")
#declaring a variable 'total' to sum up the list contents
total = 0
#for loop iterate through the list of items
for item in my_list:
#calculating total value till the last item from list
 total = total + item
#printing the total received
print ("total is " , total)
