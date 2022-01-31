# they are extremely useful
# they make organized and powerful programs

# types of data = string text numbers boolean
# structures such as lists, dictionaries
#but not all things can be expressed in terns of these basic data types
# eg person, phone
# therefore, we create a phone data type and store every attribute of "phone"

#classes are define your own data type

#see student.py file

from student import Student
student1 = Student("Oscar", "Accounting", 3.1, False)
student2 = Student("Phyllis", "Business", 3.8, False)

print(student2.on_honor_roll()) #this is an application of class function
