#Program for file operations
#initialising the my_filename variable with logfile.txt string 
my_filename = "logfile.txt"
#Try Method
try:
#Opening a file named logfile.txt and append as file handle
 with open(my_filename, "a") as file_handle:
  print(f"Writing a test line to {my_filename}")
#Writing "Test line" to the file  
  file_handle.write("Test line")
#Except statement for IO errors 
except IOError as err:
 print(f"IOError was {err}")
#Except statement for EOF Error
except EOFError as err:
 print(f"End of file error was {err}")
#Except statement for OS Error
except OSError:
 print("OS Error")
#Except statement for other Errors
except:
 print("General Error")
#if all good, print file is created
else:
 print("File created")
#Final part programs execution
finally:
 print("Finishing up!")
 # close not needed because with statement
 # file_handle.close()