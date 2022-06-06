from random import randint
from random import choice


condition = 'What is the result of the expression?'


def question_and_answer():
    a = randint(1, 50)
    b = randint(1, 30)
    operations = ['-', '+', '*']
    x = (choice(operations))
    expression = f'{a} {x} {b}'
    right_answer = str(eval(expression))
    return (expression, right_answer)
