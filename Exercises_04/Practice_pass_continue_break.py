my_list = [1,2,3,0]
for my_number in my_list:
 if my_number == 1:
  pass
 if my_number == 2:
  continue
 if my_number == 3:
  print(f"Found the number {my_number}")
 if my_number == 0:
  break
