#to loop over various collection of numbers, string, data

for letter in "Giraffe Academy":
    print(letter)

#looping through all of the letters in giraffe academy

friends = ["Jim", "Karen", "Kevin"]
for friend in friends: #can also loop through an array
    print(friend)

for index in range(10): #to loop through numbers
    print(index) #leaves out 10 tho

for index in range(3,10): #3 to 9 is printed
    print(index)

#get the length of array or number of elements
len(friends)
for index in range(len(friends)):
    print(friends[index]) #accessing by index value using len to get the length = 3
#looping through array is a common use of for loop

for index in range(5):
    if index == 0:
        print("This is the first iteration. ")
    else:
        print("Not first. ")

#exponent functions

print(2**3) # this is 2 raised to the third power

def raise_to_power(base_num, pow_num):
    result = 1 #have a variable to store results
    for index in range(pow_num):
        result = result * base_num
    return(result) #use return to end the function as it enhances usability of the function

print(raise_to_power(3,4))
print(raise_to_power(29,9))

#lists and nested loops

number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]         #this is a grid of 4 rows and three columns kinda
]
#can make list of lists

print(number_grid[0]) #prints entire row
print(number_grid[0][0]) # prints 0th row and 0th column
print(number_grid[2][1])

#nested for loops
for row in number_grid: #passing a list to the for loop accesses it by 0,1,2.. indices
    #print(row) #prints entire list of list
    for col in row:
        print(col)
#2D list printing code