#program for calculating the CPU utilization and log
#Importing module file_utilities and functions path_name, log_file_name
from file_utilities import path_name, log_file_name
#Importing module os_utilities and functions detect_os,cpu_load
from os_utilities import detect_os,cpu_load
#Importing time module and sleep function
from time import sleep
# Check the OS in use, and figure out a log file name and path
this_os = detect_os()
log_path = path_name()
#Opening a .csv file
filename = log_file_name(".csv")
print(log_path + filename)
# Loop forever
while True:
 # Sleep for 1 second
 sleep(1)
 # Get a time stamp for this line
 timestamp = log_file_name("")
 # Get some information
 information = cpu_load()
 # Create a line for the logfile, convert the integer values to string
 logline = timestamp + ":" + str(information[0]) + "," + str(information[1]) + "\n"
 # Now write it to the logfile
 try:
#using append as file handle, writing to the file with value on logline
  with open(filename, "a") as file_handle:
   print(f"logging to {filename}")
   file_handle.write(logline)
# if there is IO error print it  
 except IOError as err:
  print(f"IOError was {err}")
# if there is EOF error print it
 except EOFError as err:
  print(f"End of file error was {err}")
# if there is OS error print "OS Error"  
 except OSError:
  print("OS Error")
#if any other error print as "General Error"
 except:
  print("General Error")