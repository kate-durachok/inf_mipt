import turtle
turtle.hideturtle()
turtle.color("indigo")
turtle.pensize(5)
import turtle

turtle.speed(0)
turtle.tracer(False)
turtle.setheading(90)

def vosem(r, n):
    while n >= 0:
        turtle.circle(r)
        turtle.circle(-r)
        r = r + 10
        n = n - 1

vosem(50, 15)

turtle.tracer(True)


turtle.exitonclick()
