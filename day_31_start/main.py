from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
GERMAN_FONT = ("Ariel", 30, "italic")
ENGLISH_FONT = ("Ariel", 40, "bold")
timer_id = ''
current_card = {}


try:
    data = pandas.read_csv("data/words_to_learn.csv")
except (FileNotFoundError, pandas.errors.EmptyDataError):
    original_data = pandas.read_csv("data/German_Top_100.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

# ------------------------------------- Read Data ------------------------------------- #
def next_card():
    global timer_id, current_card
    if timer_id:
        display.after_cancel(timer_id)
    current_card = choice(to_learn)

    canvas.itemconfig(canvas_image, image=card_front_image)
    canvas.itemconfig(card_title, text="German", fill="black")
    canvas.itemconfig(card_word, text=current_card["German"], fill="black")
    timer_id = display.after(3000, flip_card)

# ------------------------------------- Flip the Card ------------------------------------- #
def flip_card():
    canvas.itemconfig(canvas_image, image=card_back_image)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")

# ------------------------------------- Remove the remembered Card ------------------------------------- #
def remove_card():
    to_learn.remove(current_card)
    next_card()

# ------------------------------------- Save CSV when program closes ------------------------------------- #
def on_close():
    new_df = pandas.DataFrame(to_learn)
    new_df.to_csv("data/words_to_learn.csv", index=False)  # Save before closing
    display.destroy()

# Display
display = Tk()
display.title("Flashy")
display.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# Canvas
canvas = Canvas(master=display, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0, bd=0)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400,263,image=card_front_image)
card_title = canvas.create_text(400, 150, text="Title", font=GERMAN_FONT)
card_word = canvas.create_text(400,263, text="Word", font=ENGLISH_FONT)
canvas.grid(row=0, column=0, columnspan=2)

# Button
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, bd=0, bg=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, bd=0, bg=BACKGROUND_COLOR, command=remove_card)
right_button.grid(row=1, column=1)

next_card()

display.protocol("WM_DELETE_WINDOW", on_close)
display.mainloop()