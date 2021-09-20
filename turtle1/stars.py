import turtle
turtle.hideturtle()
turtle.color("gold")
turtle.pensize(10)
import turtle

turtle.speed(0)
turtle.tracer(False)


def star(n, l):
    if n % 2 != 0 :
        for i in range(n):
            turtle.forward(l)
            fi = n // 2 * 360 / n
            turtle.right(fi)
    else:
        n = n + 1
        star(n, l)

star(5, 150)

turtle.tracer(True)

turtle.exitonclick()
