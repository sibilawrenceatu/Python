#Program for creating class template
"""
Class template by Sibi
27OCT22: Primary
"""
#Defining class MyTemplate
class MyTemplate():
 # Constructor, called whenever an instance of the class is created.
 def __init__(self, attribute1: str, attribute2: bool) -> None:
  print("Constructor ran")
 # Take in an argument and assign it to a meaningful attribute name
  self.attr1 = attribute1
  self.attr2 = attribute2
 #initialise class variables with 0 value as this is a template. Change the values as per requirement. 
 class_object_attribute1 = 0
 class_object_attribute2 = 1
#sample method 
 def method1(self):
  method_value="test"
  print(method_value) 

# Instantiate the class
my_object1 = MyTemplate("test", True)
# Check the object
print(my_object1.class_object_attribute1, my_object1.class_object_attribute2)
#calling sample method in my_object1
my_object1.method1()
