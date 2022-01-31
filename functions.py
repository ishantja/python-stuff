#collection of codes that perform a specific task
#you can just call the function next time you want to do the same thing
#it is a core concept in python

#create a function that says hi! to the user

def say_hi (name,age): # keyword def     function name    (parameters)   : start function
    #needs indentation to say code is inside the function
    print("Hello " + name +", you are " + str(age)) # but you need to call the function for it to have any effect

print("Top")
say_hi("Ishan", 24) #type out the function name with whatever argument it takes
    # in this case we have no arguments
print("Bottom")
#this is the flow of program exectution when it involves functions
#usually named in lower cases and put underscore for spaces

#parameters can also be given
say_hi("Steve", 70)
#it is better to group your programs in to various functions

#return statement
#when we want to get information back form a function

#cube a number
def cube(num):
    return num*num*num
    print("code") #anything after return is not going to get executed

print(cube(3)) #only shows none as the function did not return anything

result = cube(4)
print(result)

#if statements in python . This is how we can make the program make decisions
#conditional statement

is_male = False
is_tall = True
if is_male or is_tall: #when one of this is true, statement gets executed
    print("You either a male or are tall" )
else:
    print("You are neither male nor tall")
if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but are tall")
else:
    print("You are either not male or not tall or both")

#we can also use comparison operators instead of boolean operators for conditions

#if statements with comparisons

#python function to find the biggest number
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
         return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(300,40,5.5))
#we could also compare strings, booleans, numbers and strings
# num == num0 menans both are equal ? != IS NOT EQUAL TO > < >= <=

#building a better calculator in python
num1 = float(input("Enter first number: ")) #runs the risk of user entering string and running into an error
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print (num1- num2)
elif op == "/":
    print(num1/num2)
elif op == "*" or op == "x" or op == "X":
    print (num1*num2)
else:
    print("Please enter a valid operator")

