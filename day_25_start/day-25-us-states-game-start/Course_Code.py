import turtle
import pandas

# SCREEN SETUP
screen = turtle.Screen()
screen.title("US State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# TURTLE SETUP
t = turtle.Turtle()
t.hideturtle()
t.penup()

# MANAGING DATA
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

# GAME LOGIC
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt=f"What's another state name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("State_to_Learn")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(answer_state)

# DISPLAYING ALL STATES NAMES ON THE SCREEN
remaining_states = [item for item in all_states if item not in guessed_states]
for state_remain in remaining_states:
    state_data = data[data.state == state_remain]
    t.goto(state_data.x.item(), state_data.y.item())
    t.write(state_remain)

screen.exitonclick()