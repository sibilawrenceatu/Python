#Program for demonstrating raise exception
"""
Validate integer function with raise exception
"""
def validate_integer():
# Loop forever
 while True:
  try:
# Take an input number as a string and convert it to an integer
   my_value = int(input("Enter an integer greater than 0"))
#if statement for checking the my_value is less than or equal to zero and raise exception if it matches
   if my_value <= 0:
    raise Exception("Values must be > 0")
#else part execution if the value is greater than zero
   else:
    print("Validation checks passed")
  except:
# Bad value,
   print("Error")
#Continue statement to return to the while loop   
   continue
#if all good, print valid input
  else:
   print("Valid input")
# Good value, exit the loop
   break
  finally:
# Only runs after the except, continue
   print("Try again - enter an integer value only!")
#calling the function validate_integer()
validate_integer()
