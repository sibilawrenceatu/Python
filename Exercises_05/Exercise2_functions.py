#Exercise3 - finding a number in a list using functions
#defined function 'find_num' which gets a list 'number_list' and an integer 'number'. The function will try to find whether 'number' is available in the list or not.
def find_num(number_list: list, number: int)->bool:
 """
 The find_num() function is using for identifying whether a number is available on the given list 
 """
#'for' loop for iteration through the list 'number_list' 
 for iterate_number in number_list:
#if condition checking whether each iterated number from the list matches to the 'number'
  if iterate_number == number:
#If the 'iterate_number' matches the 'number' then boolean value True will be returned
   return True
  else:
# If the condition is false for each iteration then passing
   pass
#calling the function 'find_num' and passing a list of values and the number to be checked. The result returned from function will be saved to 'result' variable.
result = find_num([1,2,3,4,5,6,7,8], 9)
#printing the result
print("output from lecturer's program is " ,result)
#The function is using an if statement. If the condition is passed then only it will return a boolean value. If the condition is false, then it returns nothing. Hence the program returns None value.
#The function will return True only if the number to be checked is from 1 to 8. Otherwise the number 9 should be included in the list values to get a True value in return.


#The function can be modified as below to get the False value in return
#defined function 'find_num' which gets a list 'number_list' and an integer 'number'. The function will try to find whether 'number' is available in the list or not.
def find_num(number_list: list, number: int)->bool:
 """
 The find_num() function is using for identifying whether a number is available on the given list 
 """
#'for' loop for iteration through the list 'number_list'
 for iterate_number in number_list:
#flag variable is created and made it a global variable to assign 0 value to flag variable.
  global flag
#calculated the length of list file
  length = len(number_list)
#Incrementing global flag value by 1
  flag = flag + 1
#if condition checking whether each iterated number from the list matches to the 'number'
  if iterate_number == number:
#If the 'iterate_number' matches the 'number' then boolean value True will be returned
   return True
#If the iterated_number do not match the 'number' then checking if it reached the end of 'length' of list. This condition will work through the iteration as long as first IF statement is false.
#If the flag set is not reached the end of 'length' then it will pass. Once the flag is equal to the length then there is no more value to be checked from the list and this elif will not execute after that.
  elif flag<length:
   pass
#When both if and elif are not executed the else statement will execute and set the boolean value to False and return
  else:
   return False
#Setting the flag to 0 for initialization.   
flag = 0
#calling the function 'find_num' and passing a list of values and the number to be checked. The result returned from function will be saved to 'result' variable.
result = find_num([1,2,3,4,5,6,7,8], 9)
#printing the result
print("output from edited program is " ,result)
