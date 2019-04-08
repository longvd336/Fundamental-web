from turtle import*

def draw_square(length, color):
    speed(1)   
    shape()
  
    pencolor(color)

    for i in range(4):
        fd(length)
        right(90)

    mainloop()

draw_square(100,"red" )