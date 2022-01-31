from math import *


print('Hello World')
print("   /|")
print("  / |")
print(" /  |")
print("/___|")

character_name = 'Mike'
character_age = '35'


print("There once was a man named " + character_name + ", ")
print("he was " + character_age + " years old. ")

character_name = "Tom"
character_age = 50
is_male = True # this is a boolean data type
is_female = False # this is also stored as 0

print("He really liked the name, " + character_name + ", ")
print("but didn't like being " + str(character_age) + ".")

#data type learned: string, numbers, and boolean
# numbers can store integers, and decimals

print("\n")
print("Giraffe\"s Academy") #use backslash to render the following character as is

phrase = "Giraffe Academy"
print(phrase+"\n")

#string concatination
print (phrase + "is cool.")

#functions with string
print(phrase.lower())
print(phrase.upper())
print(phrase.isupper())
print(len(phrase))
print(phrase[0]) #access each value of the string. start's with zero
print(phrase[3])
print(int(phrase.index("G")))#returns index of a particular character within a string

#lot of clutter. move on to replace function
print(phrase.replace("Giraffe", "Eleplant"))
print(phrase)

#learn all the string functions as a good measure because we use it regularly

#now we move on to numbers
#awesome functions, operations etc etc
print("\n\n")
print(2)
print(54)
print(2.0987)
print(3*(4+5))
print(10 % 3 ) # this is 10 mod 3. gives the remainder
#store numbers inside a variable
my_num = 5
print(my_num)
print(str(my_num) +" is my favourite number")

#common number functions
#abs
my_num = -5
print(abs(my_num))
#pow = power of the number
print(pow(3,2))
print(pow(3,6))
#max = returns the larger of two numbers
print(max(4,6))
print(min(4,6))
print(round(3.7))

#importing means importing other files

my_num = -5
print(ceil(3.7))#grab the roundest number
print(floor(3.7))# returns the lowest nearest integer

print (int(sqrt(36)))
print(sqrt(149))

#ask user input

# name =  input("Enter your name:")
# age =  input("Enter your age:")
# print ("Hello, " + name +"! You are " + age)

#store it in name variable and use as you please. concatinate and everything
#input is good to get user engagement

#create two variables. store two numbers. add those two.

num1 = input("Enter first number:") #this is stored as string
num2 = input("Enter second number:") #this as well
#sum =  int(num1) + int(num2) #typecasting to integer number
sum =  float(num1) + float(num2) #use float because it is versatile
print("The sum of the two numbers is " + str(sum))

#now that we created a student class
# we can create an object

from student import Student

student1 = Student(Ishan, Robotics, 3.52, False)
#object is just an instance of a class
print(student1)
#all attributes are also accessible
print(student1.major)
#this is essentially a student data type

student2 = Student("Pamela","Art", 3.1, False)
print(student2)