#Exercise 3 - checking the even numbers in the list provided with True or False
#Defined the search_even function to check the even numbers in a list 'number_list' passed as argument
def search_even(number_list: list)->bool:
 """
 search_even () function checks the even numbers in the given list and returns boolean values
 """
#length of the passed list is calculated and stored in variable length.
 length = len(number_list)
#setting the flag to 0 as initialisation
 flag = 0
# for loop is applied to iterate throught the list number_list
 for item in number_list:
# to check the even numbers, need to check whether the modulus operation gives 0
  if item % 2 == 0:
#Returning the bollean value True if a even number is found
   return True
#Increasing the flag by 1
   flag += 1
#Elif applied to see whether the check is happening till the end of the list
  elif flag < (length-1):
#Increasing the flag by 1
   flag += 1
#Pass is applied to continue with operation
   pass
#if all the above conditions in IF and ELIF are false, the else will apply which will return False boolean value which means there are no even numbers in the list
  else:
   return False
#function search_even is called with a list of values and the return value from function is stored on to result variable
result = search_even([1,5,87,95,55,38,53,97])
#Printing the boolean value result returned
print ("The result obtained is " ,result)
