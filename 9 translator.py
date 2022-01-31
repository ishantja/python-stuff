# #Giraffe language
# vowels -> g
#  -----------------
#
# dog -> dgg
# cat -> cgt
#

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou": #special in python to check something is in something else
        #if letter.lower()  in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation

#print(translate(input("Enter a phrase to translate: ")))

# for loop used in conjumnction with an if statement
#but the  problem is if we start with a capital vowel so the first letter wil be small "g"

#commenting is so fun and I have been using it since the very first tutorial
print("Comments are fun")

'''
you can comment in here as well 
this is something new
I like it 
so efficient 
Just use triple quotations!
'''

#comments are also useful for debugging

#try except block to fish out errors
#you don't want something small to trip up your entire program
#try accept will try out a block of code

try:
    #value = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError:
    print("Divide by zero")
except ValueError:
    print('Invalid input')

#we can store error as a variable
'''except ZeroDivisionError as err: # this stores the error in the err variable 
    print(err)
except ValueError'''