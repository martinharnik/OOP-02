from turtle import *

def triangle(t, size, width, color):
    size = int(size)
    width = int(width)
    t.color(color)
    t.width(width)
    t.begin_fill()
    for i in range(2):
        t.forward(size)
        t.left(90)
    t.end_fill()

def pentagon(t, width, color):
    width = int(width)
    t.width(width)
    t.color(color)
    for i in range(5):
        t.forward(100)
        t.left(72)

def square(t, size, width, color):
    size = int(size)
    width = int(width)
    t.width(width)
    t.color(color)
    for i in range(4):
        t.forward(size)
        t.left(90)

bob = Turtle()

ask = input("Enter shape:").lower()
while ask != "Done":
    if ask == "triangle":
        size = int(input("Enter size: "))
        width = int(input("Enter width: "))
        col = input("Enter color: ")
        triangle(bob, size, width, col)
    elif ask == "pentagon" :
        width = int(input("Enter width: "))
        col = input("Enter color: ")
        pentagon(bob, width, col)
    elif ask == "square" :
        size = int(input("Enter size: "))
        width = int(input("Enter width: "))
        col = input("Enter color: ")
        square(bob, size, width, col)
    else:
        print("No shape entered")
    ask = input("Enter shape: ")
done()