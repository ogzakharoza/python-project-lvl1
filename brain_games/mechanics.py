import random
from random import randint
from math import gcd
from brain_games.prime import isPrime


def welcome_user():

    name = input('May I have your name? ')

    return name


def game():

    print('Answer "yes" if the number is even, otherwise answer "no"')

    for i in range(3):
        num = randint(1, 100)
        print(f'Question: {num}')
        ask = input('Your answer: ')
        if num % 2 == 0 and ask == 'yes':
            print('Correct!')
        elif num % 2 != 0 and ask == 'no':
            print('Correct!')
        else:
            return False
    return True


def calc():

    print('What is the result of the expression?')
    for i in range(3):
        a = randint(1, 50)
        b = randint(1, 30)
        operations = ['-', '+', '*']
        x = (random.choice(operations))
        expression = eval(str(a) + x + str(b))
        print(f'Question: {a} {x} {b} = ?')
        answ = int(input('Your answer: '))
        if answ == expression:
            print('Correct')
        else:
            return False
    return True


def game_gcd():

    print('Find the greatest common divisor of given numbers.')
    for i in range(3):
        a = randint(1, 100)
        b = randint(1, 100)
        x = gcd(a, b)
        print(f'Question: {a} {b}')
        answ = int(input('Your answer: '))
        if answ == x:
            print('Correct')
        else:
            return False
    return True


def game_progression():
    print('What number is missing in the progression?')
    for i in range(3):
        progr_list = []
        a = randint(1, 100)
        x = randint(1, 6)
        b = a + 9 * x + 1
        for i in range(a, b, x):
            progr_list.append(i)
        index = randint(0, len(progr_list) - 1)
        q = progr_list[index]
        progr_list[index] = '..'
        print('Question:', *progr_list)
        answ = int(input('Your answer: '))
        if answ == q:
            print('Correct!')
        else:
            print(f'{answ} is wrong answer ;(. Correct answer was {q}')
            return False
    return True


def brain_prime():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for i in range(3):
        n = randint(0, 100)
        print(f'Question: {n}')
        answ = input('Your answer: ')
        if isPrime(n) and answ == 'yes':
            print('Correct!')
        elif not isPrime(n) and answ == 'no':
            print('Correct!')
        elif n == 0 and answ == 'yes':
            return False
        elif n == 1 and answ == 'yes':
            return False
        else:
            return False
    return True
