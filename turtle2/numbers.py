import turtle
import math

turtle.hideturtle()
turtle.color("sky blue")
turtle.pensize(3)
turtle.speed(0)
turtle.up()


def forw(k):
    turtle.forward(k)


def down():
    turtle.down()


def up():
    turtle.up()


def zero(x, y):
    turtle.goto(x, y)
    down()
    turtle.setheading(90)
    forw(50)
    turtle.right(90)
    forw(25)
    turtle.right(90)
    forw(50)
    turtle.right(90)
    forw(25)
    up()


def one(x, y):
    turtle.goto(x, y + 25)
    down()
    turtle.setheading(45)
    forw(25 * math.sqrt(2))
    turtle.right(135)
    forw(50)
    up()


def two(x, y):
    turtle.goto(x, y + 50)
    down()
    turtle.setheading(0)
    forw(25)
    turtle.right(90)
    forw(25)
    turtle.right(45)
    forw(25 * math.sqrt(2))
    turtle.left(135)
    forw(25)
    up()


def three(x, y):
    turtle.goto(x, y)
    down()
    turtle.setheading(45)
    forw(25 * math.sqrt(2))
    turtle.left(135)
    forw(25)
    turtle.right(135)
    forw(25 * math.sqrt(2))
    turtle.left(135)
    forw(25)
    up()


def four(x, y):
    turtle.goto(x, y + 50)
    down()
    turtle.setheading(-90)
    forw(25)
    turtle.left(90)
    forw(25)
    turtle.left(90)
    forw(25)
    turtle.left(180)
    forw(50)
    up()


def five(x, y):
    turtle.goto(x, y)
    down()
    turtle.setheading(0)
    forw(25)
    turtle.left(90)
    forw(25)
    turtle.left(90)
    forw(25)
    turtle.right(90)
    forw(25)
    turtle.right(90)
    forw(25)
    up()


def six(x, y):
    turtle.goto(x, y + 25)
    down()
    turtle.setheading(0)
    for i in range(0, 4):
        forw(25)
        turtle.right(90)
    turtle.left(45)
    forw(25 * math.sqrt(2))
    up()


def seven(x, y):
    turtle.goto(x, y)
    down()
    turtle.setheading(90)
    forw(25)
    turtle.right(45)
    forw(25 * math.sqrt(2))
    turtle.left(135)
    forw(25)
    up()


def eight(x, y):
    turtle.goto(x, y)
    down()
    turtle.setheading(90)
    for i in range(0, 4):
        forw(25)
        turtle.right(90)
    forw(25)
    for i in range(0, 4):
        forw(25)
        turtle.right(90)
    up()


def nine(x, y):
    turtle.goto(x, y)
    down()
    turtle.setheading(45)
    forw(25 * math.sqrt(2))
    turtle.left(45)
    for i in range(0, 4):
        forw(25)
        turtle.left(90)


N = [zero, one, two, three, four, five, six, seven, eight, nine]


def number(s):
    a = [int(s[i]) for i in range(len(s))]
    x_0 = len(a) / 2.0 * (-40)
    for i in a:
        N[i](x_0, 0)
        x_0 += 40

number("16122003")

turtle.exitonclick()
