#Program for displating the current date and time in a human readable format
#Importing datetime module
from datetime import datetime as dt
# Get the current time, returns a value like 2022-10-09 17:46:45.151666
today = dt.now()
print(today)
# Get Unix time, returns a value like 1665566809.057217
unix_epoch_time = dt.timestamp(today)
print(unix_epoch_time)
#Converting the day using %d format
day = dt.now().strftime("%d")
#Converting the month using %B format
month = dt.now().strftime("%B")
#Converting the year using %Y format
year = dt.now().strftime("%Y")
#Printing the current date in human readable format
print ("date is : ",day,"-",month,"-",year)
#Converting the hour using %H format
Hour = dt.now().strftime("%H")
#Converting the minutes using %M format
Min = dt.now().strftime("%M")
#Converting the Seconds using %S format
Sec = dt.now().strftime("%S")
#Printing the current time in human readable format
print ("time is : ",Hour,":",Min,":",Sec)
