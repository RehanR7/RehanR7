from turtle import Turtle

FONT = ("Courier", 24, "normal")
GAME_OVER_FONT = ("Courier", 26, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(-280, 260)
        self.score = 1
        self.write(f"Level: {self.score}", align= "center", font=FONT)

    def add_score(self):
        self.clear()
        self.score += 1
        self.write(f"Level: {self.score}", align="center", font=FONT)

    def game_over(self):
            self.goto(0, 20)
            self.write("Game Over", align="center", font= GAME_OVER_FONT)
            self.goto(0, -20)
            self.write(f"You scored {self.score} points", align="center", font= GAME_OVER_FONT)


