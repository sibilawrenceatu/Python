#Program demonstrating class objects
"""
Class template by JOR
Revision History
06OCT22: Alpha
"""
class MyTemplate():
 # Constructor, called whenever an instance of the class is created.
 def __init__(self, attribute1: str, attribute2: bool) -> None:
  print("Constructor ran")
 # Take in an argument and assign it to a meaningful attribute name
  self.attr1 = attribute1
  self.attr2 = attribute2
#Declaring variables within class
 class_object_attribute1 = 6378137
 class_object_attribute2 = 6356752 

# Instantiate the class
my_object = MyTemplate("John", True)
# Printing the variable from my_object
print(my_object.class_object_attribute1, my_object.class_object_attribute2)
