from random import randint
import math

condition = 'Find the greatest common divisor of given numbers.'


def question_and_answer():
    a = randint(1, 100)
    b = randint(1, 100)
    c = math.gcd(a, b)
    return (f'{a} {b}', str(c))
