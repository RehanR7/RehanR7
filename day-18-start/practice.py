"""
import turtle
tim = turtle.Turtle

from turtle import Turtle
tim = Turtle()
"""

"""
for _ in range(4):
    tom.forward(100)
    tom.left(90)
"""

"""
for _ in range(15):
    tom.pendown()
    tom.pensize(1)
    tom.pencolor("pink")
    tom.forward(5)
    tom.penup()
    tom.forward(5)   
"""

"""
colors = ["red", "blue", "green", "yellow", "pink", "black", "gray", "brown"]

for sides, col in zip(range(3, 11), colors):
    angle = 360 / sides
    tom.pensize(2)
    tom.pencolor(col)
    tom.pendown()
    for _ in range(sides):
        tom.right(angle)
        tom.forward(100)

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tom.forward(100)
        tom.right(angle)

for shape_sides_n in range(3, 11):
    tom.pencolor(random.choice(colors))
    draw_shape(shape_sides_n)
"""