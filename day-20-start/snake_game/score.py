from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Nordic Light", 12, "normal")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(x=0, y=275)
        self.score = 0
        with open("highest_score.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.color("white", "black")
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score {self.high_score}", move=False,align= ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highest_score.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_score_board()

    def increase_score(self):
        self.score += 1
        self.update_score_board()

