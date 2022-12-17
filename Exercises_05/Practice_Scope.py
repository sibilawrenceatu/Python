#Program for understanding the scope of a variable
#my_string variable initialised 
my_string = "global"
#defined function my_function
def my_function():
 """
 This function used to check the value of a variable with in this function and nested_function()
 """
#my string variable assigned with "enclosing" value which only has local scope within function my_function
 my_string = "enclosing"
#A nested_function() defined within my_function
 def nested_function():
#my string variable assigned with "local" value which only has local scope within function nested_function
  my_string = "local"
#printing the value of my string within nested_function()
  print(my_string)
#Calling the nested function within my_function()
 nested_function()
#Return the value of my string to the called function my_function()
 return my_string
# Print the variable my_string
print(my_string)
# Print the output of the function, my_function
print(my_function())
help (my_function)