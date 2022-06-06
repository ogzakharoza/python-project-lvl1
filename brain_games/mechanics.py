import prompt


def start(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print(game.condition)
    NUMBER_OF_ROUNDS = 3
    for _ in range(NUMBER_OF_ROUNDS):
        right_answer = game.question_and_answer()
        print(f'Question: {right_answer[0]}')
        answer = input('Your answer: ')
        if right_answer[1] == answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;("
                  f"Correct answer was '{right_answer[1]}'.")
            print(f"Let's try again, {name}")
            return False
    print(f'Congratulations, {name}!')
