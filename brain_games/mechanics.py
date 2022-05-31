import prompt

def mechanics(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print(game.condition)
    NUMBER_OF_ROUNDS = 3
    for _ in range(NUMBER_OF_ROUNDS):
        game.question_and_answer()
        print(f'Question:{game.question}')
        answer = input('Your answer: ')
        if str(game.right_answer) == player_answer:
            print('Correct!')
        else:
            return print(f"{answer} is wrong answer ;(. Correct answer was {right_answer}.\nLets' try agan, {name}")
    print(f"Let's try again, {name}!")
