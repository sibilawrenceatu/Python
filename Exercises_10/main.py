#main module program for the OS and path files
#importing file_utilities and os_utilities
from file_utilities import path_name, log_file_name
from os_utilities import detect_os
# Check the OS in use, and figure out a log file name and path
this_os = detect_os()
log_path = path_name()
filename = log_file_name(".log")
#Printing the log_path and filename
print(log_path + filename )