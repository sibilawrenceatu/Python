#Program as part of Exercise 2 to fetch the values from a dictionary using for loop
#Dictionary scan is initialised with IP and port numbers
scan = {"192.168.3.10": "80", "192.168.3.11": "443", "192.168.3.55": "22"}
#iterate through the dictionary and print the values. This misses the port numbers from printing
for item in scan:
 print (item)
#iterate through the dictionary and print the values using dictionary.items(). This gives the format of tuples. 
for item in scan.items():
 print (item)
#iterate through the dictionary and print the values using dictionary.items() using two variables in the for loop. This prints the individual value
for ipv4, port in scan.items():
 print(f"Found a service on {ipv4} at {port}")