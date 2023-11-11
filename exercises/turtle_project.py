"""The Triforce and Hyrule Field."""

__author__ = "730664291"

from turtle import Turtle, colormode, bgcolor, done
colormode(255)
bgcolor(73, 191, 118)


def draw_star(zelda: Turtle, x: float, y: float, length: float) -> None:
    """Utilizing changing angles with triangles in order to assume the shape of a star."""
    zelda.pencolor("white")
    zelda.fillcolor("white")
    zelda.penup()
    zelda.goto(x, y)
    zelda.setheading(0.0)
    zelda.pendown()
    zelda.begin_fill()
    i: int = 0
    while i < 5:
        zelda.forward(length)
        zelda.left(144.5)
        length *= 0.98
        i += 1


def draw_yellow_triangle(zelda: Turtle, x: float, y: float, length: float) -> None:
    """Draw a yellow triangle of the given length whose bottom left corner is located at x, y to create triforce."""
    zelda.pencolor("black")
    zelda.fillcolor(242, 212, 17)
    zelda.penup()
    zelda.goto(x, y)
    zelda.setheading(0.0)
    zelda.pendown()
    zelda.begin_fill()
    i: int = 0
    while (i < 3):
        zelda.forward(length)
        zelda.left(120)
        i += 1
    zelda.end_fill()


def draw_white_triangle(zelda: Turtle, x: float, y: float, length: float) -> None:
    """Draw a white triangle of the given length whose top left corner is located at x, y to whiten middle of triforce."""
    zelda.pencolor("black")
    zelda.fillcolor(255, 255, 255)
    zelda.penup()
    zelda.goto(x, y)
    zelda.setheading(0.0)
    zelda.pendown()
    zelda.begin_fill()
    i: int = 0
    while (i < 3):
        zelda.forward(length)
        zelda.right(120)
        i += 1
    zelda.end_fill()


def draw_tree(zelda: Turtle, x: float, y: float, length: float, width: float) -> None: 
    """Draw a rectangular tree trunk and triangular top based off the given length and width whose bottom left corner is located at x, y."""
    zelda.pencolor(120, 57, 30)
    zelda.fillcolor(120, 57, 30)
    zelda.penup()
    zelda.goto(x, y)
    zelda.setheading(0.0)
    zelda.pendown()
    zelda.begin_fill()
    i: int = 0
    while (i < 4):
        if ((i % 2) == 0):
            zelda.forward(width)
            zelda.left(90)
            i += 1
        else:
            zelda.forward(length)
            zelda.left(90)
            i += 1
    zelda.end_fill()
    zelda.pencolor(14, 74, 25)
    zelda.fillcolor(14, 74, 25)
    zelda.penup()
    zelda.left(90)
    zelda.forward(length)
    zelda.left(90)
    zelda.forward(width)
    zelda.pendown()
    zelda.begin_fill()
    idx: int = 0
    while (idx < 3):
        if idx < 2:
            zelda.right(120)
            zelda.forward(width * 3)
            idx += 1
        else:
            zelda.right(120)
            zelda.forward(width * 3)
            idx += 1
    zelda.end_fill()


def draw_moon(zelda: Turtle, x: float, y: float, radius: float) -> None:
    """Draw a white full circle that starts at x, y."""
    zelda.pencolor("white")
    zelda.fillcolor("white")
    zelda.penup()
    zelda.goto(x, y)
    zelda.setheading(0.0)
    zelda.pendown()
    zelda.begin_fill()
    zelda.circle(radius, 360)
    zelda.end_fill()


def draw_mountain(zelda: Turtle, x: float, y: float) -> None:
    """Draw a gray triangle of the given length whose bottom left corner is located at x, y to represent mountains."""
    zelda.pencolor(252, 255, 253)
    zelda.fillcolor(107, 110, 108)
    zelda.penup()
    zelda.goto(x, y)
    zelda.setheading(0.0)
    zelda.pendown()
    zelda.begin_fill()
    for i in range(3):
        zelda.forward(300)
        zelda.left(120)
    zelda.end_fill()


def main() -> None:
    """The entrypoint of my scene."""
    zelda: Turtle = Turtle()
    zelda.hideturtle()
    zelda.speed(0)
    zelda.penup()
    zelda.goto(-400, 500)
    zelda.pendown
    zelda.color("black")
    zelda.begin_fill()
    for i in range(2):
        zelda.forward(800)
        zelda.right(90)
        zelda.forward(400)
        zelda.right(90)
    zelda.end_fill()
    draw_yellow_triangle(zelda, -100, -100, 100)
    draw_yellow_triangle(zelda, 0, -100, 100)
    draw_yellow_triangle(zelda, -50, -13.4, 100)
    draw_white_triangle(zelda, -50, -13.4, 100)
    draw_tree(zelda, -125, -200, 70, 20)
    draw_tree(zelda, 250, -200, 70, 20)
    draw_tree(zelda, 200, -300, 70, 20)
    draw_tree(zelda, -200, -250, 70, 20)
    draw_tree(zelda, -288, -300, 70, 20)
    draw_tree(zelda, -263, -200, 70, 20)
    draw_tree(zelda, 0, -230, 70, 20)
    draw_tree(zelda, -90, 0, 70, 20)
    draw_tree(zelda, 100, 50, 70, 20)
    draw_tree(zelda, -240, -40, 70, 20)
    draw_tree(zelda, 100, -300, 70, 20)
    draw_tree(zelda, 130, -85, 70, 20)
    draw_tree(zelda, 290, -95, 70, 20)
    draw_mountain(zelda, 100, 75)
    draw_mountain(zelda, 15, 50)
    draw_star(zelda, -300, 200, 25)
    draw_star(zelda, -200, 300, 25)
    draw_star(zelda, -180, 218, 25)
    draw_star(zelda, -168, 268, 25)
    draw_star(zelda, 0, 260, 25)
    draw_star(zelda, 48, 150, 25)
    draw_star(zelda, -80, 131, 25)
    draw_star(zelda, -250, 120, 25)
    draw_star(zelda, -90, 200, 25)
    draw_star(zelda, -170, 143, 25)
    draw_star(zelda, -90, 300, 25)
    draw_moon(zelda, -300, 250, 100)
    done()

    
if __name__ == "__main__":
    main()