from turtle import *
from random import randint

t = Turtle()

t.width(5)

for i in range(4):

    x = randint(-600, 400)
    y = randint(-200, 300)

    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    col = (r/255, g/255, b/255)

    t.up()
    t.goto(x, y)
    t.down()

    t.color(col)
    t.begin_fill()
    for i in range(4):
        t.forward(100)
        t.left(90)
    t.end_fill()

done()