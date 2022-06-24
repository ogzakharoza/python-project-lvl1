import prompt


NUMBER_OF_ROUNDS = 3


def start(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print(game.CONDITION)
    for _ in range(NUMBER_OF_ROUNDS):
        question, right_answer = game.question_and_answer()
        print(f'Question: {question}')
        answer = input('Your answer: ')
        if right_answer == answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;("
                  f"Correct answer was '{right_answer}'.")
            print(f"Let's try again, {name}!")
            return False
    print(f'Congratulations, {name}!')
