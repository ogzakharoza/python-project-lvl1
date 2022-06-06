from random import randint


condition = 'What number is missing in the progression?'


def question_and_answer():
    progr_list = []
    a = randint(1, 50)
    x = randint(1, 6)
    b = a + 9 * x + 1

    for i in range(a, b, x):
        progr_list.append(str(i))
    index = randint(0, len(progr_list) - 1)
    q = progr_list[index]
    progr_list[index] = '..'
    question = ' '.join(progr_list)
    return (question, str(q))
