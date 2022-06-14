from random import randint
import math

condition = 'Find the greatest common divisor of given numbers.'
START = 1
END = 100


def question_and_answer():
    a = randint(START, END)
    b = randint(START, END)
    c = math.gcd(a, b)
    return (f'{a} {b}', str(c))
