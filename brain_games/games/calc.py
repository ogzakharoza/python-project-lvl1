from random import randint
from random import choice


condition = 'What is the result of the expression?'

def question_and_answer():
    a = randint(1, 50)
    b = randint(1, 30)
    operations = ['-', '+', '*']
    x = (choice(operations))
    expression = eval(str(a)+x + str(b))
    question = f'Question: {a} {x} {b} = ?'
    right_answer = expression
    return right_answer, question

