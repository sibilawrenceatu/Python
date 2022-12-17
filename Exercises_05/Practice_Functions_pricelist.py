def most_expensive(price_list):
 """
 Iterate through a list and find the most expensive item
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
# Provide the data
price_list = [("Pineapple", 1.0), ("Apples", .5), ("Pears", .7), ("Peaches", .8)]
# Call the function and unpack its return values
product, price = most_expensive(price_list)
#Running the below code will give an error as there are only two items in the tuple and we are trying to get a value for "availability" variable too
#product, price, availability = most_expensive(price_list)
print(product, price)