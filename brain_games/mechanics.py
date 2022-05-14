from random import randint

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
        break

