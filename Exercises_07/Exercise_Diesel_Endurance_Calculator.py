#Exercise program for Diesel generator endurance calculator 
"""
Diesel endurance calculator
Sibi 2022
"""
#function for diesel endurance calculator
def diesel_check():
#Loop forever until user enter the correct inputs
 while True:
#accepting the user inputs for fules and current fuel consumption per minute and converting both values to float.
  try:
   fuel = float(input("Enter current diesel fuel in litres "))
   fuel_consumption = float(input("Enter current diesel consumption per minute in litres "))
#Calculating the total endurance in float
   endurance = float((fuel/fuel_consumption))
  except:
#Bad value entered, try again
   print("Error \n")
#message for user to enter valid digits
   print("Try again - Make sure you entered valid value for fuel and fuel consuption")
#message for user to enter a non zero value
   print("make sure you have not entered a zero value for fuel consumption")
#Continue statement for entering correct value by returning to loop
   continue
#if the user enter valid values, calculate the endurance using else block codes
  else:
   print("Valid inputs")
#print(f"the endurance of diesel generator is {endurance} minutes")
   print(f"the endurance of diesel generator is {round(endurance,2)} minutes")
#if Good value entered, exit the loop
   break
#Calling the function diesel_check
diesel_check()
