
import turtle

turtle.shape('arrow')
turtle.color("black")
k = 45
n = 360
while n > 0:
    turtle.forward(50)
    turtle.stamp()
    turtle.goto(0,0)
    turtle.left(k)
    n = n - k




