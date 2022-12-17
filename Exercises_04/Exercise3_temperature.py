#Exercise3 - converting temperature from air conditioning system in kelvin to celsius and fahrenheit
#List containing temperature in kelvin is initialised from air conditioning system
temp_in_kelvin = [300, 302, 290, 295, 305, 285]
#Converting to celsius using formula and using list comprehension to make list temp_in_celsius containing converted temperature in celsius and printing 
temp_in_celsius = [(temp-273.15) for temp in temp_in_kelvin]
print (temp_in_celsius)
#Converting to Fahrenheit using formula and using list comprehension to make list temp_in_fahrenheit containing converted temperature in fahrenheit and printing
temp_in_fahrenheit = [(((9/5)*(temp-273.15)) + 32) for temp in temp_in_kelvin]
print (temp_in_fahrenheit)
