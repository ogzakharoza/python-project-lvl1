#!/usr/bin/env python
from brain_games.cli import welcome_user
from brain_games.mechanics import brain_prime


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print(f'Hello, {name}')
    ok = brain_prime()
    if ok:
        print(f'Congratulations, {name}')


if __name__ == '__main__':
    main()
