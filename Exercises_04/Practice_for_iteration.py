# program to iterate over a string
# setting flag to 0, flag will change to 1 if the required character is found from string
flag=0
#test string is 'Sibi Lawrence'
for test_letter in "Sibi Lawrence":
 # Specify which letter to test for
 if test_letter == "i":
  # Found the test letter
  print(f"Woo hoo, found a {test_letter}!")
  flag=1
  # Exit the current loop as soon as the test character is found
  break
#checking current flag status to know whether character found or not
if flag == 0:
 print ("test letter cannot be found")

