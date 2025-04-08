import pandas
from turtle import Screen, Turtle

class Logic:
    def __init__(self):
        self.writer = Turtle()
        self.writer.hideturtle()
        self.writer.penup()
        self.screen = Screen()
        self.data = pandas.read_csv("50_states.csv")
        self.all_states = self.data.state
        self.total_states = len(self.data.state)
        self.correct_answer = 0
        self.coordinate_list = []
        self.guessed_states_list = []

    def prompt(self):
        self.answer_state = self.screen.textinput(title=f"{self.correct_answer}/{self.total_states}",
                                                  prompt="What's another State's name?")

    def get_coordinates(self):
        for guess in self.all_states:
            if self.answer_state.lower() == guess.lower():
                self.guessed_state = guess
                self.correct_answer += 1
                correct = self.data[self.data.state == guess]
                x_coordinate = correct.x.item()
                y_coordinate = correct.y.item()
                x_y_coordinates = (x_coordinate, y_coordinate)
                self.coordinate_list.append(x_y_coordinates)
                self.guessed_states_list.append(guess)

    def write_name(self):
        if self.coordinate_list:
            x_y_coordinate = self.coordinate_list[-1]
            self.writer.goto(x_y_coordinate)
            self.writer.write(self.answer_state, align="center", font=("Arial", 12, "normal"))
