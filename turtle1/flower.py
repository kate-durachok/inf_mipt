import turtle
turtle.hideturtle()
turtle.color("salmon")
turtle.pensize(6)
import turtle

turtle.speed(0)
turtle.tracer(False)

def vosem(r, n):
    k = 360
    while k >= 0:
        turtle.circle(r)
        turtle.circle(-r)
        turtle.left(n)
        k = k - n

vosem(50, 40)

turtle.tracer(True)


turtle.exitonclick()
