import turtle
import time
import random

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PADDLE_SPEED = 20
BALL_SPEED = 3
WIN_SCORE = 5

# Paddle class
class Paddle(turtle.Turtle):
    def __init__(self, position):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def move_up(self):
        if self.ycor() < SCREEN_HEIGHT / 2 - 50:
            self.sety(self.ycor() + PADDLE_SPEED)

    def move_down(self):
        if self.ycor() > -SCREEN_HEIGHT / 2 + 50:
            self.sety(self.ycor() - PADDLE_SPEED)

# Ball class
class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = BALL_SPEED
        self.y_move = BALL_SPEED
        self.move_speed = 0.03

    def move(self):
        self.setx(self.xcor() + self.x_move)
        self.sety(self.ycor() + self.y_move)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9  # Increase speed after each paddle hit

    def reset_position(self, direction):
        self.goto(0, 0)
        self.move_speed = 0.03
        self.x_move = BALL_SPEED if direction == "right" else -BALL_SPEED
        self.y_move = random.choice([-BALL_SPEED, BALL_SPEED])

# Score class
class Score(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, SCREEN_HEIGHT // 2 - 50)
        self.write(self.left_score, align="center", font=("Courier", 24, "normal"))
        self.goto(100, SCREEN_HEIGHT // 2 - 50)
        self.write(self.right_score, align="center", font=("Courier", 24, "normal"))

    def left_point(self):
        self.left_score += 1
        self.update_score()

    def right_point(self):
        self.right_score += 1
        self.update_score()

    def game_over(self, winner):
        self.goto(0, 0)
        self.write(f"Game Over! {winner} wins!", align="center", font=("Courier", 24, "normal"))

# Game class
class Game:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.screen.bgcolor("black")
        self.screen.title("Pong")
        self.screen.tracer(0)

        self.paddle_left = Paddle((-SCREEN_WIDTH // 2 + 50, 0))
        self.paddle_right = Paddle((SCREEN_WIDTH // 2 - 50, 0))
        self.ball = Ball()
        self.score = Score()

        self.is_paused = False
        self.setup_keyboard()

    def setup_keyboard(self):
        self.screen.listen()
        self.screen.onkeypress(self.paddle_left.move_up, "w")
        self.screen.onkeypress(self.paddle_left.move_down, "s")
        self.screen.onkeypress(self.paddle_right.move_up, "Up")
        self.screen.onkeypress(self.paddle_right.move_down, "Down")
        self.screen.onkeypress(self.toggle_pause, "p")

    def toggle_pause(self):
        self.is_paused = not self.is_paused

    def play(self):
        while True:
            if not self.is_paused:
                self.screen.update()
                time.sleep(self.ball.move_speed)
                self.ball.move()

                # Top and bottom collision
                if self.ball.ycor() > SCREEN_HEIGHT // 2 - 20 or self.ball.ycor() < -SCREEN_HEIGHT // 2 + 20:
                    self.ball.bounce_y()

                # Paddle collisions
                if (self.ball.xcor() > SCREEN_WIDTH // 2 - 60 and self.ball.distance(self.paddle_right) < 50) or \
                   (self.ball.xcor() < -SCREEN_WIDTH // 2 + 60 and self.ball.distance(self.paddle_left) < 50):
                    self.ball.bounce_x()

                # Score points
                if self.ball.xcor() > SCREEN_WIDTH // 2:
                    self.score.left_point()
                    if self.score.left_score >= WIN_SCORE:
                        self.score.game_over("Left Player")
                        break
                    self.ball.reset_position("right")

                if self.ball.xcor() < -SCREEN_WIDTH // 2:
                    self.score.right_point()
                    if self.score.right_score >= WIN_SCORE:
                        self.score.game_over("Right Player")
                        break
                    self.ball.reset_position("left")

        self.screen.exitonclick()

# Start the game
if __name__ == "__main__":
    game = Game()
    game.play()