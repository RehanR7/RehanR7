from random import random
from turtle import Turtle, Screen
from random import randint

is_game_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter the color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []


x_axis = -230
y_axis = -100

for col in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(col)
    new_turtle.penup()
    new_turtle.goto(x=x_axis, y=y_axis)
    all_turtles.append(new_turtle)
    y_axis += 40

if user_bet:
    is_game_on = True

while is_game_on:
    for turtle in all_turtles:
        rand_distance = randint(0, 10)
        turtle.forward(rand_distance)
        if turtle.xcor() > 230:
            is_game_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! the {winning_color} turtle is the winner!")
            else:   
                print(f"You lost! the {winning_color} turtle is the winner!")


screen.exitonclick()