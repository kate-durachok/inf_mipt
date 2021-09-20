import turtle
turtle.hideturtle()
turtle.color("wheat")
turtle.title("smiling face")
import turtle
import math

turtle.speed(0)
turtle.tracer(False)
turtle.bgcolor("darksalmon")

def resnichki(n, k, l, x, y, color=''):
    turtle.color(color)
    while n >= 0:
        turtle.forward(l)
        turtle.goto(x, y)
        turtle.left(k)
        n = n - k

def ellipse(a, b, color='', fill=''):
    dx = turtle.xcor()
    dy = turtle.ycor()
    turtle.color(color, fill)
    turtle.begin_fill()
    for deg in range(361):
        rad = math.radians(deg)
        x = a * math.sin(rad) + dx
        y = -b * math.cos(rad) + b + dy
        turtle.goto(x, y)
    turtle.end_fill()

# причесон
ellipse(90, 120, color='black', fill='black')

# личико
ellipse(90, 110, color='wheat', fill='wheat')

# ухо намбер 1
turtle.up()
turtle.goto(90, 80)
turtle.down()
ellipse(15, 30, color='wheat', fill='wheat')

# ухо намбер 2
turtle.up()
turtle.goto(-90, 80)
turtle.down()
ellipse(15, 30, color='wheat', fill='wheat')

# реснички
turtle.up()
turtle.goto(-45,120)
turtle.pensize(5)
turtle.down()
resnichki(180, 15, 20, -45, 120, color='black')
turtle.setheading(0)
turtle.up()
turtle.goto(45,120)
turtle.down()
resnichki(180, 15, 20, 45, 120, color='black')


# глаза

turtle.color("white")
turtle.up()
turtle.goto(-45, 100)
turtle.down()
ellipse(20, 15, color='white', fill='white')
turtle.up()
turtle.goto(45, 100)
turtle.down()
ellipse(20, 15, color='white', fill='white')

# радужка  зрачки  блики

turtle.up()
turtle.goto(-44.5, 100)
turtle.down()
ellipse(10, 10, color='slate blue', fill='slate blue')
turtle.up()
turtle.goto(44.5, 100)
turtle.down()
ellipse(10, 10, color='slate blue', fill='slate blue')
turtle.up()

turtle.goto(-45, 105)
turtle.down()
ellipse(5, 5, color='black', fill='black')
turtle.up()
turtle.goto(45, 105)
turtle.down()
ellipse(5, 5, color='black', fill='black')
turtle.up()

turtle.goto(-42, 111)
turtle.down()
ellipse(1, 1, color='white', fill='white')
turtle.up()
turtle.goto(47, 111)
turtle.down()
ellipse(1, 1, color='white', fill='white')
turtle.up()


# веки

turtle.setheading(90)
turtle.goto(65, 107)
turtle.pensize(12)
turtle.color('wheat')
turtle.down()
turtle.circle(21, 180)


turtle.up()
turtle.goto(-25, 107)
turtle.down()
turtle.pensize(12)
turtle.color('wheat')
turtle.setheading(90)
turtle.circle(21, 180)

# нос

turtle.up()
turtle.goto(-3, 60)
turtle.down()
turtle.color("tan")
turtle.pensize(5)
turtle.setheading(0)
turtle.forward(6)

# рот

turtle.up()
turtle.goto(-10, 40)
turtle.down()
turtle.setheading(-90)
turtle.color("salmon")
turtle.circle(10, 180)

# челочка

turtle.up()
turtle.goto(-85, 125)
turtle.down()
turtle.color("black")
turtle.fillcolor("black")
turtle.begin_fill()
turtle.goto(-30, 165)
turtle.goto(75, 175)
turtle.goto(55, 220)
turtle.goto(35, 235)
turtle.goto(15, 240)
turtle.goto(5, 243)
turtle.goto(-25, 240)
turtle.goto(-55, 220)
turtle.goto(-75, 190)
turtle.goto(-88, 140)
turtle.end_fill()

# бакенбарды
for y in range (115, 150, 7):
    turtle.up()
    turtle.goto(80, y)
    turtle.down()
    turtle.goto(85, y+5)
for y in range(100, 135, 7):
    turtle.up()
    turtle.goto(-80, y)
    turtle.down()
    turtle.goto(-85, y + 5)

# щечки
turtle.up()
turtle.goto(-60, 80)
turtle.down()
turtle.color("light coral")
for x in range (-60, -30, 10):
    turtle.goto(x, 80)
    turtle.down()
    turtle.goto(x + 5, 70)
    turtle.up()

for x in range(35, 65, 10):
    turtle.goto(x, 80)
    turtle.down()
    turtle.goto(x + 5, 70)
    turtle.up()

# шея
turtle.up()
turtle.goto(-20, 5)
turtle.down()
turtle.color("wheat")
turtle.fillcolor("wheat")
turtle.begin_fill()
turtle.goto(20, 5)
turtle.goto(20, -36)
turtle.right(180)
turtle.circle(-20, 180)
turtle.goto(-20, 5)
turtle.end_fill()

# футболка

turtle.up()
turtle.goto(-105, -90)
turtle.down()
turtle.color("steel blue")
turtle.fillcolor("steel blue")
turtle.begin_fill()
turtle.setheading(90)
turtle.circle(-55, 90)
turtle.forward(25)
turtle.right(90)
turtle.circle(25, 180)
turtle.right(90)
turtle.forward(25)
turtle.circle(-55, 90)
turtle.goto(-105, -90)
turtle.end_fill()



turtle.tracer(True)


turtle.exitonclick()
