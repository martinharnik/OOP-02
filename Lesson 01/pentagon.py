from turtle import *

t = Turtle()

t.width(5)
colors = ["red", "green", "blue", "orange", "black"]
for c in colors:
    t.color(c)
    t.forward(100)
    t.left(72)

done()