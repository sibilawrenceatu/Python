#Program for creating a .csv filename with time stamp
"""
copyright = "© Sibi 2022"
"""
if __name__ == '__main__':
    from datetime import datetime
else:
    from datetime import datetime
#Importing date and time from datetime library as datetime
#from datetime import datetime
#Creating function finaloutput() to give output file name
def finaloutput():
    """
copyright = "© Sibi 2022"
This function will be creating a .csv filename with time stamp prefixed with "nodes"
    
#Getting current date and time from datetime.now() function
    now = datetime.now()
#Formatting the time to a desired format of Year-Month-date-Hour-Minutes-Seconds
    now = now.strftime("%Y-%m-%d-%H-%M-%S")
#Creating the final output file name by concatinating strings "nodes" , time string obtained ,and
#".csv" to get the desired format
    final_output="nodes"+str(now)+".csv"
#Returning the final_output value to the called function
    return final_output
    """
    final_output="nodes.csv"

