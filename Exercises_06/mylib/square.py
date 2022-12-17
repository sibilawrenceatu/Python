square_text = "Yo, time to square stuff!"
def square(x):
 return x*x
if (__name__ == '__main__'):
 print(f"This module is called {__name__} and executes as a standalone script")
else:
 print(f"This module is called {__name__} and is being called by another script")
