#program to check the format function
#declaration of 3 strings
a = "I am"
b = "feeling"
c = "good"
#.format method usage
print("the message is - {first} {second} {third}".format(first = a, second = b,third = c))
#escape sequence usage
print("the escape sequence message is - \n {first} \n {second} \n {third}".format(first = a, second = b,third = c))
# formation of concatenated string from a,b and c
concatenated_string = a + " " + b + " " + c
print (f"original string is: {concatenated_string}" )
#coversion of string to upper case and printing
print (f"the upper case of string is : {concatenated_string.upper()}")
#coversion of string to lower case and printing
print (f"the lower case of string is : {concatenated_string.lower()}")
