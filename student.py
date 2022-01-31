class Student:
    #now define a bunch of attribute about student
    #don't forget to indent
    def __init__(self, name, major, gpa, is_on_probation): # this is an initialized function
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def on_honor_roll(self): #class function
        if self.gpa >= 3.5:
            return True
        else:
            return False
