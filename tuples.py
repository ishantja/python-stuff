#tuple is a type of data structure
# similar to lists
# can hold multiple pieces of information
# it has some key differences from lists tho

#to create x,y coordinates

coordinates = (4,5) #make tuple using ()
#tuples are immutable
#it is final and absolute at the time of creation
print(coordinates[0])
print(coordinates[1])
#accessed using index values same as lists
#coordinates[1] = 10 #does not support item assignment; cannot modify

#coordinates are good candidates for tuple as they don't need appending

coordinates = [(4,5),(6,7), (80,30)] #this is a list of tuples
print(coordinates)

