from random import randint
import math

CONDITION = 'Find the greatest common divisor of given numbers.'
START = 1
END = 100


def question_and_answer():
    a = randint(START, END)
    b = randint(START, END)
    right_answer = str(math.gcd(a, b))
    question = f'{a} {b}'
    return question, right_answer
