import turtle
import time

turtle.hideturtle()
turtle.color("grey")
turtle.pensize(3)
turtle.speed(0)

turtle.up()
X = turtle.window_width()
turtle.goto(X/2, 0)
turtle.down()
turtle.goto(-X/2, 0)

turtle.pensize(3)
turtle.color("dodger blue")

Vx = 10
Vy = 30
g = -2
x = -X/2
y = 0
dt = 0.3

while x < X/2:
    x += Vx * dt
    y += Vy * dt + g * dt**2 / 2.0
    Vy += g * dt
    if y <= 0:
        Vy *= -0.8
        Vx *= 0.8
        y = 0
    turtle.goto(x, y)

turtle.exitonclick()
