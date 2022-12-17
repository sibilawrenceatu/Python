#Program for importing modules
#importing cube module as mycube
import mylib.cube as mycube
#Importing square module as mysquare
import mylib.square as mysquare
#Print the values from imported cube module by passing values
print(mycube.cube_text, mycube.cube(3))
#Print the values from imported square module by passing values
print(mysquare.square_text, mysquare.square(3))