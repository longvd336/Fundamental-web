from random import *

def generate_quiz():
    # Hint: Return [x, y, op, result]
    import random
    import calculate
    x = randint(1,10)
    y = randint(1,10)

    op = choice(["+", "-", "*", "//"])
    
    result = calculate.tinhToan( x , y, op )

    fake = randint(result-1 , result + 1 )
    
    return [x, y, op , fake]

def check_answer(x, y, op, fake , answer):
    
    import calculate
    result = calculate.tinhToan( x , y, op )
    if fake == result:
        if(answer == True):
            return True
        else:
            return False

    if fake != result:
        if(answer == False):
            return True
        else:
            return False
    # pass
