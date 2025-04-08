#TODO: Extract color list from the image file using colorgram module!
"""
import colorgram

color_list = colorgram.extract("image.jpg", 50)
color_palette = []

for color in color_list:
    rgb = color.rgb
    temp = tuple(rgb)
    color_palette.append(temp)

print(color_palette)
"""
import turtle
from turtle import Turtle, Screen
import random


color_list = [(233, 166, 59), (46, 112, 157), (113, 150, 203), (212, 123, 164),
     (171, 45, 87), (2, 177, 143), (152, 18, 54), (224, 201, 117), (224, 77, 115),
     (162, 166, 36), (28, 35, 83), (227, 87, 43), (42, 166, 208), (119, 172, 116),
     (119, 102, 158), (215, 64, 34), (41, 54, 97), (77, 22, 44), (226, 171, 189),
     (20, 94, 69), (32, 61, 55), (158, 210, 197), (14, 87, 102), (183, 188, 207),
     (225, 176, 167), (160, 202, 217), (133, 35, 25), (71, 28, 13), (83, 79, 23)]

"""
slime = Turtle()
turtle.colormode(255)
slime.hideturtle()
slime.penup()
y_coordinates = range(30, 330, 30)

def move_forward():
    for _ in range(10):
        slime.dot(15, random.choice(color_list))
        slime.forward(30)

def go_up():
    for y in y_coordinates:
        move_forward()
        slime.teleport(x=0, y=y)


go_up()
"""

slime = Turtle()
turtle.colormode(255)
slime.speed(0)
slime.hideturtle()
slime.penup()
slime.setheading(225)
slime.forward(300)
slime.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    slime.dot(20, random.choice(color_list))
    slime.forward(50)

    if dot_count % 10 == 0:
        slime.setheading(90)
        slime.forward(50)
        slime.setheading(180)
        slime.forward(500)
        slime.setheading(0)



screen = Screen()
screen.exitonclick()