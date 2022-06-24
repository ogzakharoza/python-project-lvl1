from random import randint
from random import choice


CONDITION = 'What is the result of the expression?'

OPERATIONS = ['-', '+', '*']

START = 1

END = 100


def question_and_answer():
    a = randint(START, END)
    b = randint(START, END)
    operator = choice(OPERATIONS)
    expression = f'{a} {operator} {b}'
    if operator == '-':
        right_answer = a - b
    elif operator == '+':
        right_answer = a + b
    elif operator == '*':
        right_answer = a * b
    return (expression, str(right_answer))
