from random import *

shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]

def get_shapes():
    return shapes

def generate_quiz():
    elements = choice(shapes)
    color = elements["text"].upper()
    more_color = [ '#3F51B5','#C62828','#FFD600','#4CAF50']
    code = choice(more_color)

    return [
                color,
                code ,
                randint(0,1)   # randint(0,1)          # 0 : meaning, 1: color
            ]

def mouse_press(x, y, color , code , quiz_type):
    from Se_5 import is_inside
    l = [x,y]
    if(quiz_type == 0):
        for item in shapes:
            text = item["text"].upper()
            i = item["rect"]
            
            if color == text :
                
                return is_inside( l , i )
                # if(i[0] < x <i[0]+i[2] and i[1]< y < i[1]+i[3]):
                #     return True
            
                # else:
                #     return False
    if(quiz_type == 1):
        for item in shapes:
            
            c = item["color"]
            i = item["rect"]
            
            if c == code:
                
                return is_inside( l , i)
            #     if(i[0] < x <i[0]+i[2] and i[1]< y < i[1]+i[3]):
            #         return True
            
            #     else:
            #         return False
                 


        
        
    
    
    

