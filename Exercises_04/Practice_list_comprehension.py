#program for list comprehensions
#A string my_string is initialised
my_string = "Morning Folks!"
#Generating letter by letter from my_string to my_list variable and printing the list
my_list = [letter for letter in my_string]
print(my_list)
#saving numbers 0 - 19 to my_list variable and printing the list
my_list = [number for number in range(0,20)]
print(my_list)
#saving numbers 0 - 19 after multiply with 10 to my_list variable and printing the list
my_list = [number * 10 for number in range(0,20)]
print(my_list)
#saving numbers 0 - 9 after multiply with 10 to my_list variable and printing the list using if
my_list = [number * 10 for number in range(0,20) if number < 10]
print(my_list)
#Conversion program
#declaring conversion amount in 'conversion' variable
conversion = 0.3048
#List containing depth in feet is initialised
my_depth_in_feet = [12.3, 13.8, 15.3, 12.1, 8.8]
#calculating the conversion for the list values and printing using comprehensions
my_depth_in_meters = [(depth * conversion) for depth in my_depth_in_feet]
print(my_depth_in_meters)