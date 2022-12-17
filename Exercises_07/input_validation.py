#Program for input validation
"""
Function for input validations
"""
#defining function validate_integer
def validate_integer():
# Loop forever
 while True:
#Try block for getting the user input 
  try:
   user_input = int(input("Enter an integer value: "))
#Except statement for any errors
  except:
# Bad value,
   print("Error")   
# Continue statement used to return to the while loop and accept the input from user again
   continue
  else:
   print("Valid input")
 # Good value, exit the loop
   break
  finally:
 # Only runs after the except, continue
   print("Try again - enter an integer value only!")
#Calling the validate_integer function
validate_integer()
