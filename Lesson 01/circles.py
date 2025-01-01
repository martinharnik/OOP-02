from turtle import *
from random import randint

t = Turtle()

t.color("blue")
t.width(5)

for i in range (10):
    x = randint(-400, 400)
    y = randint(-100, 300)
    random_radius = randint(10, 50)
    
    t.up()
    t.goto(x, y)
    t.down()

    t.begin_fill()
    t.circle(random_radius)
    t.end_fill()

done()