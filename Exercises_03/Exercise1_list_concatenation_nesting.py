#my list 1 contents
my_list1 = ["sibi",45,5.67,'a']
#printing my list contents
print ("the contents of first list is ",my_list1)
#creating a slice from my_list1
mylist_slice = my_list1[1]
#printing the 2nd item from the list
print ("the list item on the 1st index is " ,mylist_slice)
#my list 2 contents
my_list2 = [1,"test",'W',"hello","good morning"]
print ("the contents of second list is ",my_list2)
#concatenated list (mylist_1 and my_list2)
my_concat_list = my_list1 + my_list2
print ("the contents of concatenated list is ",my_concat_list)
#nested list (mylist_1 and my_list2)
my_nested_list = [my_list1,my_list2]
print ("the contents of nested list is ",my_nested_list)
#replacement of item at index 2 (5.67) of concatenated list with string "how are you ?"
my_concat_list[2] = "how are you ?"
#printing modified concatenated list
print ("the modified concatenated list is ",my_concat_list)
#Appending 67890 to the concatenated list and printing new list
my_concat_list.append(67890)
print ("the concatenated list contents after appending 67890 is ",my_concat_list)
#Removing 'sibi' from the concatenated list and printing new list
my_concat_list.remove("sibi")
print ("the concatenated list contents after removal of 'sibi' is ",my_concat_list)
#Inserting 'thanks' to the concatenated list at index 2 and printing new list
my_concat_list.insert(2,"thanks")
print ("the concatenated list contents after insertng 'thanks' on 2nd index is  ",my_concat_list)
