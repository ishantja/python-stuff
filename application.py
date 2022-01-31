from question import Question

question_prompts = [
    "What color are apples? \n(a) Red/Green \n(b) Purple\n(c) Orange\n\n",
    "What color are bananas? \n(a) Teal \n(b) Yellow\n(c) Magenta\n\n",
    "What color are strawberries? \n(a) Red \n(b) Blue\n(c) Yellow\n\n",
]

questions = [
    Question(question_prompts[0],"a"),
    Question(question_prompts[1],"b"),
    Question(question_prompts[2],"a")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score +=1
    print("You got " + str(score) + "/" +str(len(questions)) +" correct")

run_test(questions)

#we can also create class functions.
#see student.py

