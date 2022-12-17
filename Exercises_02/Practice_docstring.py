
def most_expensive(price_list):
 """
Script: Practice_docstring.py
By: Sibi
Purpose: This program unpack the tuple
 """
 # Set up the variables
 max_price = 0
 max_price_item = ""
 # Iterate, unpacking the tuple
 for description, price in price_list:
 # If this is the maximum price, record that in our variables
  if price > max_price:
   max_price = price
   max_price_item = description
 # If it is not the maximum price, do nothing
  else:
   pass
 # Return the maximum prices item and its price
 return max_price_item, max_price
help (most_expensive)