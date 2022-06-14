from random import randint

condition = 'Answer "yes" if the number is even, otherwise answer "no".'
START = 1
END = 100


def question_and_answer():
    n = randint(START, END)
    if n % 2 == 0:
        return (n, 'yes')
    return (n, 'no')
