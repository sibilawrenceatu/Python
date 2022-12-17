#Program showing constructor usage
"""
Simple Class by JOR, by convention, use camel case to name classes
"""
# Create a class
class JORzClass():

# Constructor, called whenever an instance of the class is created.
 def __init__(self, my_greeting):
  print("Running constructor for JORzClass")
# Create attributes and set initial values
  self.message = my_greeting
# A function my_method within class   
 def my_method(self):
  print(self.message)
#Creating my_class1 class variable
my_class1 = JORzClass("Morning JOR!")
#Calling through function my_method
my_class1.my_method()
#Printing class type
print(type(my_class1))
