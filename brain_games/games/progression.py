from random import randint


CONDITION = 'What number is missing in the progression?'

START_A = 1
END_A = 50

START_X = 1
END_X = 6

NUMBERS_IN_PROGRESSION = 9


def question_and_answer():
    progression = []
    start = randint(START_A, END_A)
    step = randint(START_X, END_X)
    end = start + NUMBERS_IN_PROGRESSION * step + 1

    for i in range(start, end, step):
        progression.append(str(i))
    index = randint(0, len(progression) - 1)
    right_answer = str(progression[index])
    progression[index] = '..'
    question = ' '.join(progression)
    return question, right_answer
