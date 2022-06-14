from random import randint
from random import choice


condition = 'What is the result of the expression?'

OPERATIONS = ['-', '+', '*']

START = 1

END = 100


def question_and_answer():
    a = randint(START, END)
    b = randint(START, END)
    x = choice(OPERATIONS)
    expression = f'{a} {x} {b}'
    if x == '-':
        right_answer = a - b
    elif x == '+':
        right_answer = a + b
    elif x == '*':
        right_answer = a * b
    return (expression, str(right_answer))
