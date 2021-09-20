import turtle
turtle.hideturtle()
turtle.color("black")
turtle.pensize(3)
import turtle

turtle.speed(0)
turtle.tracer(False)


turtle.setheading(90)
turtle.up()
turtle.goto(350, 0)
turtle.down()

def vosem(r, n):
    while n >= 0:
        turtle.circle(r,180)
        r_1 = r / 10
        turtle.circle(r_1, 180)
        n = n - 1

vosem(30, 12)

turtle.tracer(True)


turtle.exitonclick()
