from random import randint
from random import choice


condition = 'What is the result of the expression?'

OPERATIONS = ['-', '+', '*']

def question_and_answer():
    A = randint(1, 100)
    B = randint(1, 100)
    X = choice(OPERATIONS)
    expression = f'{A} {X} {B}'
    if X == '-':
        right_answer = A - B
    elif X == '+':
        right_answer = A + B
    elif X == '*':
        right_answer = A * B
    return (expression, str(right_answer))
