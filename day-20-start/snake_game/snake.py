from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.x_axis = 0
        self.body_parts = []
        self.create_snake()
        self.head = self.body_parts[0]

    def create_snake(self):
        # Create the initial body parts of the snake
        for _ in range(3):
            new_part = Turtle(shape="square")
            new_part.penup()
            new_part.color('black', 'white')
            new_part.goto(x=self.x_axis, y=0)
            self.x_axis -= 20
            self.body_parts.append(new_part)

    def add_part(self):
        position = self.body_parts[-1].position()
        new_part = Turtle(shape="square")
        new_part.penup()
        new_part.goto(position)
        new_part.color('black', 'white')
        self.body_parts.append(new_part)

    def reset_snake(self):
        for seg in self.body_parts:
            seg.goto(1000,1000)
        self.body_parts.clear()
        self.create_snake()
        self.head = self.body_parts[0]

    def move(self):
        # Move the body parts in reverse order
        for segment in range(len(self.body_parts) - 1, 0, -1):
            new_x = self.body_parts[segment - 1].xcor()
            new_y = self.body_parts[segment - 1].ycor()
            self.body_parts[segment].goto(x=new_x, y=new_y)
        # Move the head forward
        self.head.forward(20)

# CONTROLS
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
