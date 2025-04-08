from turtle import Turtle

class Border(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()


    def upper_border(self):
        self.goto(0, 310)
        self.shapesize(0.5,40)

    def lower_border(self):
        self.goto(0, -310)
        self.shapesize(0.5,40)

    def right_border(self):
        self.goto(395, 0)
        self.shapesize(31, 0.5)

    def left_border(self):
        self.goto(-395, 0)
        self.shapesize(31, 0.5)