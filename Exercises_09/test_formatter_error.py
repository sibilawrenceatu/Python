#Program for format testing with forceful error values
#Importing unit test modules
import unittest
#Importing formatter modules
import formatter
#Defining TestFormatter class
class TestFormatter(unittest.TestCase):
#test_lower method within class
 def test_lower(self):
#initialise value for test_text 
  test_text = "JOHN ORAW"
#result value get back the value returuning from convert_lower() function
  result = formatter.convert_lower(test_text)
#Checking whether the result value equal to a string using assertEqual function
  self.assertEqual(result, "john oraw")
#test_upper method within class
 def test_upper(self):
#initialise value for test_text
  test_text = "John ORaw"
#result value get back the value returuning from convert_upper() function
  result = formatter.convert_upper(test_text)
#Checking whether the result value equal to a string using assertEqual function
  self.assertEqual(result, "JoHN ORAW")
#Checking whether the program runs from this module and if so call the function unittest.main()
if __name__ =="__main":
 unittest.main()
