from Question_Class import Question

#Create the list of questions as well as the list of multi-choice options.

question_list = [
    "What color are apples? \n (a) Red/Green \n (b) Purple \n (c) Orange \n",
    "What color are bananas? \n (a) Yellow \n (b) Orange \n (c) Red \n",
    "What color are strawberries \n (a) Orange  \n (b) Yellow \n (c) Red \n  "
]


questions = [
    #call the question class to set the question aprompt and the correct answer
    Question(question_list[0], 'a'),
    Question(question_list[1], 'a'),
    Question(question_list[2], 'c')
]

#input = list of questions we want to ask a user3
def run_test(questions):
    score = 0
    for question in questions:
        if question.answer == input(question.prompt):
            score += 1
    print("You got " + str(score) + " question(s) right out of " + str(len(questions)) + " questions.")

run_test(questions)