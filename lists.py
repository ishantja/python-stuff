#large amount of data can be organized
#it is a structure that takes a bunch of different data values
#common use cases demonstrated

friends = ['Kevin', 'Karen', 'Jim', 2 , True, False ] #[] is associated with list
#can store multiple values in the same variable

#can be accessed with index position. starts with 0 tho.
print(friends)
print(friends[1:5])
print(friends[-1]) #indexing from the back of the list
print (friends[-3]) #first from the backward is -1
print(friends[1:]) # 1 to all aftwewards
print(friends[1:3]) #1 to upto 3 but not including 3

# can also modify elements from the list
friends[1] = 'Mike'
print(friends[1])
#add, delete, copy

#list functions . list is one of the most important structure in pyton

lucky_numbers = [4,8,15,16,23,42] # can store milllions of values like these. so we have some handy functions.
# thankfully . :)
friends = [ "Kevin", "Karen", "Jim", "Jim", "Oscar", "Tom"]
# friends.extend(lucky_numbers) # can add another list to the end of the list
friends.append("Creed") # additional item at the end of the list
friends.insert(1,'Kelly') #inserrt(index, value). all other values will be pushed off to the right
friends.remove("Jim") # removes anything you want
#friends.clear() #nothing is left in the list
friends.pop() # removes the last element in the list. or pops it off
# to check for a certain value
print(friends.index("Kevin"))


#to count the number of similar elements
print(friends.count("Jim"))
friends.sort() # will put to alphabetical order
lucky_numbers.sort()


print(friends)
lucky_numbers.reverse()
print(lucky_numbers)

#can copy a list as well
friends2 = friends.copy()

print(friends2)