#This program is a demo of a map function
def double_number(n: int)->int:
 """
 Simple function to double a number
 """
 return n+n
# Create a list of numbers for testing
my_numbers = [1,2,3,4,5]
# Map my_numbers to the double_number function, return type is map
result = map(double_number, my_numbers)
# Print a list of the map
print(list(result))
# For iterate through map
for item in map(double_number, my_numbers):
 print(item)
