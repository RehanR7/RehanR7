import turtle
from logic import Logic


screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

logic = Logic()


is_game_on = True
while is_game_on:
    logic.prompt()
    logic.get_coordinates()
    logic.write_name()



screen.mainloop()