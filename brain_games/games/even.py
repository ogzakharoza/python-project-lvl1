from random import randint

condition = 'Answer "yes" if the number is even, otherwise answer "no".'


def question_and_answer():
    n = randint(1, 100)
    if n % 2 == 0:
        return (n, 'yes')
    return (n, 'no')
