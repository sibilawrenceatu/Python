#Walkthrough 4 exercise 
#When a, b and C are true
print ("first check starting with a,b and c are true")
a = True
b = True
c = True
if a:
 print("a was true")
elif b:
 print("b was true")
elif c:
 print("c was true")
else:
 print("None of our boolean variables were true")
print ("first check exiting")
#When a is false, b and C are true
print ("second check is starting with a is false,b and c are true")
a = False
b = True
c = True
if a:
 print("a was true")
elif b:
 print("b was true")
elif c:
 print("c was true")
else:
 print("None of our boolean variables were true")
print ("second check exiting")
#When a and b are false, and C is true
print ("third check is starting with a and b are false,and c is true")
a = False
b = False
c = True
if a:
 print("a was true")
elif b:
 print("b was true")
elif c:
 print("c was true")
else:
 print("None of our boolean variables were true")
print ("third check exiting")
#When a, b and c are false
print ("fourth check is starting with a,b and c are false")
a = False
b = False
c = False
if a:
 print("a was true")
elif b:
 print("b was true")
elif c:
 print("c was true")
else:
 print("None of our boolean variables were true")
print ("fourth check exiting")