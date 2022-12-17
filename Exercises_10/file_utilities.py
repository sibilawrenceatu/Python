""""
File utilities, forked from the Comm module of SD-Node, written c. 2017
Tested with Python >=3.6
By: JOR
 v0.1 26AUG21
"""
from datetime import datetime as dt
import sys, csv
def path_name():
 # Operating system dependent stuff
 this_os = sys.platform
 if this_os == 'win32':
  return './logfiles/'
 elif this_os == 'linux':
  return '/home/pi/logfiles/'
 else:
  print(f'Unsupported OS: {this_os}')
 exit(0)
def log_file_name(extension):
 """
 Create a file name in the logfiles directory, based on current data and time
 Requires the computer to have an RTC or synched clock
 """
 now = dt.now()
 # Linux
 file_name = '%0.4d%0.2d%0.2d-%0.2d%0.2d%0.2d' % (now.year, now.month, now.day, now.hour, now.minute, now.second)
 return file_name + extension
if (__name__ == '__main__'):
 print(f"This module is called {__name__} and executes as a standalone script")
 log_path = path_name()
 filename = log_file_name(".log")
 print(log_path + filename )
else:
 pass
 #print(f"This module is called {__name__} and is being called by another script")