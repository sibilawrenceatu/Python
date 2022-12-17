#This is a program for opening a log file, Iterate through it,
#and get the required fields and write it to a .csv file
"""
copyright = "© Sibi 2022"
"""

if __name__ == '__main__':
 #Importing dhcpack function from dhcp_acknowledgement.py file from Source folder
    from dhcp_acknowledgement import dhcpack
#Importing datetimefunction from output_filename from Sources folder as final_output
    from output_filename import finaloutput as final_output
else:
#Importing dhcpack function from dhcp_acknowledgement.py file from Source folder
    from Source.dhcp_acknowledgement import dhcpack
#Importing datetimefunction from output_filename from Sources folder as final_output
    from Source.output_filename import finaloutput as final_output
def log_operation():
    """
Function for extracting information from the DHCP log
    """
    mac_list = []
#opening the log file in read only mode and saving data in it to "logfile" variable
    logfile= open("dhcpd.log",'r')
#Using "for" loop for traversing through the dhcpd.log file line by line
    for iteration in logfile:
#Creating required_string string variable to store value
#in each line from log file from the 34th character
        required_string = iteration[34:]
#Creating list_of_values list by removing the blank spaces using split method
        list_of_values = required_string.split(" ")
#Checking the first value of list list_of_values with the string DHCPACK
        if list_of_values[0] == "DHCPACK":
#Additional check using "if" statement if the 4th field of list_of_values
#contains "via" instead of a mac address. If found, ignore the line and
#"continue" the loop as they contain the duplicate mac address fields
            if list_of_values[4] == "via":
#continue statement used for continuing the loop if a "via" key word match
#is found, else passing to next line of code
                continue
            else:
                pass
#An if statement checking whether current mac address value in list_of_values[4]
#is already available in the list mac_list. If found, ignore the line and continue the for loop
                if list_of_values[4] in mac_list:
#Continue the loop using continue statement
                    continue
#If the mac address in above if statement do not match the mac_list,
#then follow the codes to add the mac address to the list using else statement.
#This is to find unique mac addresses
                else:
#appending currently searched mac address to the list mac_list as it is a unique value
                    mac_list.append(list_of_values[4])
#Calling the function dhcpack from from dhcp_acknowledgement.py and passing the current
#list_of_values as argument, then storing the return value to final_list
                    final_list = dhcpack(list_of_values)
#Modifying the final_list content with required format and values
                    final_list = final_list[0]+", "+final_list[1]+", "+final_list[2]+", "+final_list[3]
#Printing the modified final_list to console for reference
                    print(final_list)
#Opening a new csv file with name starting with nodes, followed by date and time stamp
#and .csv extenstion. This will make sure whenever the script runs, a new file is always
#created with current time stamp
#The open function calls another function final_output() from file output_filename.py
#for formatting the output file name and receives a timestamped filename in return
                with open(final_output(), "a") as file_handle:
#Writing the data on final_list line by line to the .csv file
                    file_handle.write(final_list+"\n")
