from turtle import *

t1 = Turtle()
t2 = Turtle()
t3 = Turtle()
t4 = Turtle()

def triangle(t, color):
    t.color(color)
    t.begin_fill()
    for i in range(3):
        t.forward(80)
        t.left(120)
    t.end_fill()


turtle = [t1, t2, t3, t4]
y = 90
for t in turtle:
    t.up()
    t.goto(0, y)
    t.down
    y -= 90

triangle(t1, "green")
triangle(t2, "red")
triangle(t3, "blue")
triangle(t4, "orange")
done()
