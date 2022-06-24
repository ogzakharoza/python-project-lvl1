from random import randint

CONDITION = 'Answer "yes" if the number is even, otherwise answer "no".'
START = 1
END = 100


def question_and_answer():
    question = randint(START, END)
    if question % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return question, right_answer
