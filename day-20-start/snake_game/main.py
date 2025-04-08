from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

# screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Snake Game")

# object initialize
snake = Snake()
food = Food()
score = Score()

# keys control
screen.listen()
screen.onkey(fun=snake.up,key="Up")
screen.onkey(fun=snake.down , key="Down")
screen.onkey(fun=snake.left , key="Left")
screen.onkey(fun=snake.right , key="Right")

# game mechanism
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # food collision system
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.add_part()
        score.increase_score()

    # detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.reset_score()
        snake.reset_snake()

    # detect collision with snake body
    for part in snake.body_parts[1:]:
        if snake.head.distance(part) < 10:
            score.reset_score()
            snake.reset_snake()

screen.exitonclick()