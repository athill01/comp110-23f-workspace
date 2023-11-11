"""Turtle Tutorial."""

from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()
bob: Turtle = Turtle()
zelda: Turtle = Turtle()
bob.speed(3000)

leo.speed(3000)

i: int = 0
while (i < 4):
    leo.forward(300)
    leo.right(90)
    i += 1

leo.penup()
leo.goto(45, 60)
leo.pendown()

bob.penup()
bob.goto(45,60)
bob.pendown()

side_length: int = 200
leo.color(103, 112, 120)
i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i += 1

side_length: int = 200
bob.color(232, 19, 29)
i: int = 0
while (i < 100):
    bob.forward(side_length)
    bob.left(123)
    side_length *= 0.97
    i += 1

zelda.pencolor("black")
zelda.fillcolor(242, 212, 17)
zelda.penup()
zelda.goto(225, 200)
zelda.setheading(0.0)
zelda.pendown()
zelda.begin_fill()
i: int = 0
while (i < 3):
    zelda.forward(50)
    zelda.left(120)
    i += 1
zelda.end_fill

done()