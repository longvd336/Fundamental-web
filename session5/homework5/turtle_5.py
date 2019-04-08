from turtle import*

def draw_star(x,y,length):
    penup()
    goto(x,y)
    pendown()
    shape()
    speed(1)
    for i in range(5):
        fd(length)
        left(216)

draw_star(-50, 50,100)

mainloop()