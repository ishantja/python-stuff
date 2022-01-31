# this is how inheritance works. inheritance in action !

# this helps to avoid copying and pasting class functions from another broader class
from inheritance import Chef
class ChineseChef(Chef): # Chef class is inherited into ChineseChef
    def make_fried_rice(self):
        print("The chef makes fried rice")
    def make_special_dish(self):
        print("The chef makes orange chicken")


