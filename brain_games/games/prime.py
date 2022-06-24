from random import randint

CONDITION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
START = 1
END = 100


def is_prime(number):
    k = 0
    for i in range(2, number // 2 + 1):
        if (number % i == 0):
            k = k + 1
    if (k <= 0):
        return True
    else:
        return False


def question_and_answer():
    a = randint(START, END)
    if is_prime(a):
        return (str(a), 'yes')
    else:
        return (str(a), 'no')
