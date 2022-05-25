from brain_games.cli import welcome_user
from brain_games.mechanics import game_progression


def main():

    print('Welcome to the Brain Games!')

    name = welcome_user()
    print(f'Hello, {name}')
    ok = game_progression()
    if ok:
        print(f'Congratulations, {name}')


if __name__ == '__main__':
    main()
