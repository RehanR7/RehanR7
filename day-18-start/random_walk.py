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

directions = [0, 90, 180, 270]
tom.width(15)
tom.speed("fastest")

for _ in range(200):
    tom.color(random_color())
    tom.forward(20)
    tom.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()