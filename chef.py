from inheritance import Chef
from ChineseChef import ChineseChef

myChef = Chef()
myChef.make_special_dish()

myChineseChef = ChineseChef()
myChineseChef.make_chicken() #notice this is not placed in the chinese chef class but still got access
myChineseChef.make_fried_rice() #this is the new function
myChineseChef.make_special_dish() #this is the overridden function

# final topic is python interpreter
# it is a sandbox envorinment to try out various lines of code
# open cmd.exe 