from random import randint

condition = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def question_and_answer():
    a = randint(1, 100)
    k = 0
    for i in range(2, a // 2 + 1):
        if (a % i == 0):
            k = k + 1
    if (k <= 0):
        return (str(a), 'yes')
    else:
        return (str(a), 'no')
