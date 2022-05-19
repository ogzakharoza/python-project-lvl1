import random
from random import randint
from random import choice
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
            print("Let's try again")
            return False
    return True

def calc():
    print(f'What is the result of the expression?')
    for i in range(3):
        a = randint(1, 50)
        b = randint(1, 30)
        operations = ['-', '+', '*']
        x = (random.choice(operations))
        expression = eval(str(a)+ x + str(b))
        print(f'Question: {a} {x} {b} = ?')
        answ = int(input('Your answer: '))
        if answ == expression:
            print('Correct')
        else:
            print("Let's try again")
            return False
    return True

