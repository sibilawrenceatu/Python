#Program demonstrating class objects
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
#defining method my_method within class
 def my_method(self):
  print(self.message)
  
#Creating my class
class MyClass1():
#Constructor for MyClass1
 def __init__(self, message1):
  self.message = message1
  #Method for MyClass1
 def functioncall(self):
  print(f"The message is {self.message}")

class MyClass2():
#Constructor for MyClass2
 def __init__(self, pvt_message1):
  self.message = pvt_message1
  #Method for MyClass2
 def class2call(self):
  print(f"The message is {self.message}")

#created first object my_class1
my_class1 = JORzClass("Morning JOR!")
#Calling function within my_class1
my_class1.my_method()
#Printing type of my_class1
print(type(my_class1))

#created second object myclass2
My_Class2 = MyClass2("'Hello' from My_Class2 object")
#Calling function class2call()within my_class2
My_Class2.class2call()
