#program to demonstrate the .format functionality and conversion of float to 3 decimal places
#declaring two numbers and calculating the float results
number1 = 1545643
number2 = 4356
result = number1/number2
#print using the .format function
print ("the result of {} divided by {} is {}".format(number1, number2, result))
#adjusting float value to 3 decimal places
print ("the float adjust valur to 3 decimal places is {r:1.3f}".format(r=result))

