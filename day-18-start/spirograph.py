import turtle
from turtle import Turtle, Screen
import random

tom = Turtle()
turtle.colormode(255)
tom.shape("arrow")
tom.color("black")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colors = (r, g, b)
    return random_colors


tom.width(1)
tom.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tom.color(random_color())
        tom.circle(100, 360, 360)
        tom.setheading(tom.heading() + size_of_gap)

draw_spirograph(5)


screen = Screen()
screen.exitonclick()