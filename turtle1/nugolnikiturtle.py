
import turtle
import math

turtle.shape('square')
turtle.color("tomato")
a = 20

for n in range (3, 20, 1):
    turtle.up()
    turtle.goto(0, 0)
    a = a + 10
    r = a / (2 * math.sin(( 2 * math.pi ) / (2 * n) ))
    turtle.setheading(0)
    #turtle.right(5 * n)
    turtle.forward(r)
    turtle.left(90 + 180 / n)
    k = n
    while k > 0:
        turtle.down()
        turtle.forward(a)
        turtle.left(360 / n)
        k = k - 1


