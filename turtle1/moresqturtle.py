
import turtle

turtle.shape('triangle')
turtle.color("pink")
for i in range(20, 100, 10):
    turtle.forward(i / 2)
    turtle.left(90)
    turtle.forward(i)
    turtle.left(90)
    turtle.forward(i)
    turtle.left(90)
    turtle.forward(i)
    turtle.left(90)
    turtle.forward(i / 2)
    turtle.right(90)
    turtle.up()
    turtle.forward(5)
    turtle.left(90)
    turtle.down()


