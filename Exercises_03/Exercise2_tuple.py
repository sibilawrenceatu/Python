#my tuple 1 contents
my_tuple1 = ("I am fine",7.9,'a')
#printing my tuple contents
print ("the contents of first tuple is ",my_tuple1)
#creating a slice from my_tuple1
mytuple_slice = my_tuple1[2]
#printing the 3rd item from the tuple
print ("the tuple item on the 2nd index is " ,mytuple_slice)
#my tuple 2 contents
my_tuple2 = (1,"Hi",'W',"hello","good")
print ("the contents of second tuple is ",my_tuple2)
#concatenated tuple (mytuple_1 and my_tuple2)
my_concat_tuple = my_tuple1 + my_tuple2
print ("the contents of concatenated tuple is ",my_concat_tuple)
#nested tuple (mytuple_1 and my_tuple2)
my_nested_tuple = (my_tuple1,my_tuple2)
print ("the contents of nested tuple is ",my_nested_tuple)
#Try of replacement of item at index 2 "a" of concatenated tuple with string "how are you ?" and gives error which shows tuples are immutable
my_concat_tuple[2] = "how are you ?"
