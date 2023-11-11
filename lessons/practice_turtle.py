"""Practicing Turtle."""

from turtle import Turtle, colormode, done
colormode(255)
zelda: Turtle = Turtle()
death: Turtle = Turtle()

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

death.right(90)
death.circle(125)

done()