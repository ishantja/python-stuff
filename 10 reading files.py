#reading from external files

employee_file = open("employees.txt", "r") #file name only if it is in the same directory , r for read, w for write, a for append at the end of the file
#r+ means read and write

#to figure out what is inside of it
#first check if the file is readable
print(employee_file.readable())
#print(employee_file.read()) #prints out all the information in the file
print(employee_file.readline()) #reads the first line and then puts the cursor to the next line
print(employee_file.readline())
print(employee_file.readlines()[1]) #this gives the line number as 1

for employee in employee_file.readlines():
    print(employee)

employee_file.close() #make sure to close the file at some point

#writing and appending files in python
employee_file = open("employees.txt","r")
print(employee_file.read())
employee_file.close()
#now to add a new employee
employee_file = open("employees.txt",'a')
employee_file.write("\nToby - Human Resources") #don't run the progarm again andn again as it will create duplicates
employee_file.write("\nKelly - Customer Service") #\n is an escape characrter
employee_file.close()

#employee_file - open("employees.txt", "w") #this will overwrite the og file
employee_file = open("employees1.txt", "w")
employee_file.write("Kelly - Customer Service")
employee_file.close()

import useful_tools #core concept in python

print(useful_tools.roll_dice(6))
# some are inside lib folder some are built-in
# some can be installed (3rd party)

#pip install
#pip is a package manager to install manage update delete python modules
#pip-install will be installed in side-packages folder

import docx

#now you can use docx module


