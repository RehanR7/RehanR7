from turtle import Screen
from paddle import Paddle
from ball import Ball
from border import Border
from score import Score
import time

screen = Screen()
screen.screensize(canvwidth=800, canvheight=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((360, 0))
l_paddle = Paddle((-360, 0))
ball = Ball()

# ScoreBoard
score = Score()

# border
up_border = Border().upper_border()
low_border = Border().lower_border()
R_border = Border().right_border()
L_border = Border().left_border()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    # Detect collision with the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 335 or ball.distance(l_paddle) < 50 and ball.xcor() < -335:
        ball.paddle_bounce()

    # Detect R side miss
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    # Detect L side miss
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

screen.exitonclick()