from turtle import Turtle, Screen


slime = Turtle()
screen = Screen()

def move_forward():
    slime.forward(10)

def move_backward():
    slime.backward(10)

def move_left():
    slime.left(30)

def move_right():
    slime.right(30)

def reset():
    slime.reset()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=reset)
screen.exitonclick()