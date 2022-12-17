#Exercise1 - divisible function returning boolean value to check whether the modulus operation returns True or False
#defined the function 'divisible' which accepts numerator and denominator in integers and return the boolean value
def divisible(numerator: int, denominator: int)->bool:
 """
 The divisible is a function which used for finding whether the passed digits are completely divisible or not
 """
#statement checking whether modulus operation gives 0 value when 30 is divided by 4
 return numerator % denominator == 0
#Printing the boolean output value
print(divisible(30,4))
#The function will return True if the numerator is a multiple of 4 or the denominator has a value of 1/2/3/5/6/10/15/30  