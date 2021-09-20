import turtle
turtle.shape('classic')
turtle.color("tan")
import math


k = 1
fi_rad = 0.1
for i in range (0, 1000):
    ro = k * fi_rad
    x = math.cos(fi_rad) * ro
    y = math.sin(fi_rad) * ro
    turtle.goto(x, y)
    fi_rad += 0.1
