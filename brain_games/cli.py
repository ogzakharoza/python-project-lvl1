import prompt


def welcome_user():
    
    name = prompt.string('Введи своё имя ')
    
    print(f'Привет, {name}')
