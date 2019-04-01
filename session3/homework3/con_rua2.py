from turtle import*


shape()
speed(1)
colors = ['red', 'blue', 'brown', 'yellow', 'grey']

n = 0
while(n<5):
    color(colors[n])
    begin_fill()
    fd(30)
    right(90)
    fd(60)
    right(90)
    fd(30)
    right(90)
    fd(60)
    right(90)
    fd(30)
    end_fill()
    n+=1

mainloop()