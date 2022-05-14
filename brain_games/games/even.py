import prompt
import mechanics

def cycle():
    correct_answers = 0
    number_of_rounds = 3
    while correct_answers < number_of_rounds:
        print mechanics.answer_check()
        if correct_answers >= number_of_rounds:
            return f'Ты победил'



    
