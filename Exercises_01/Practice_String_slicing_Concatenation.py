#Program for string concatenation and slicing
#initial word
word = "Good Morning Sibi"
print ("current word is - " + word) 
#slicing the first 4 letters from current word
word_1 = word[0:4:1]
#slicing 4 letters from 13th position
word_2 = word[13:17:1]
#Generating new words using the sliced words and new word "Evening"
new_word = word_1 + " Evening " + word_2
print ("new word is - " + new_word)

