import turtle

turtle.hideturtle()
turtle.color("sky blue")
turtle.pensize(5)
turtle.speed(0)

from random import *

while (True):
    turtle.forward(randint(20, 50))
    turtle.setheading(randint(-359, 359))

