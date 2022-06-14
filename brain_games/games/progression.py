from random import randint


condition = 'What number is missing in the progression?'

START_A = 1
END_A = 50

START_X = 1
END_X = 6


def question_and_answer():
    progr_list = []
    a = randint(START_A, END_A)
    x = randint(START_X, END_X)
    b = a + 9 * x + 1

    for i in range(a, b, x):
        progr_list.append(str(i))
    index = randint(0, len(progr_list) - 1)
    q = progr_list[index]
    progr_list[index] = '..'
    question = ' '.join(progr_list)
    return (question, str(q))
