# executes a bunch of code as long as the condition is satisfied

i = 1
while i <= 10:
    print (i)
    i +=1 #i++ is not valid in python i+= 1 is same as i = i+1
print("Done with loop")

#building a guessing game in python using all sorts of cool structures
#specify a secret word and the user can try to guess it

secret_word = "giraffe"
guess = "" #this is set to an empty string
#if they don't guess it correctly, they get to keep guessing again
guess_count = 0
guess_limit = 3
out_of_guesses = False
while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
         guess = input ("Enter guess: ")
         guess_count += 1
    else:
        out_of_guesses = True
#print("You win!")

if out_of_guesses:
    print("Out of guesses!")
else:
    print("You win!")
# implement a three try


