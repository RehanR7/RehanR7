from tkinter import *
import os
import subprocess
import pandas as pd
import random
import pygame

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
unknown_words = {}

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/German_Top_100.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def generate_audio(text, model, filename):
    command = f'echo "{text}" | /home/nano/python/my_projects/piper/piper --model {model} --output_file {filename}.wav'
    subprocess.run(command, shell=True, check=True)

def play_audio(filename):
    pygame.mixer.init()
    pygame.mixer.music.load(filename + ".wav")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        window.update()  # Ensure GUI stays responsive

    os.remove(filename)

def german_tts():
    model = "/home/nano/python/my_projects/piper/de_DE-thorsten-high.onnx"
    filename = "german_word.mp3"
    generate_audio(current_card["German"], model, filename)
    play_audio(filename)

def english_tts():
    model = "/home/nano/python/my_projects/piper/en_US-libritts-high.onnx"
    filename = "english_word.mp3"
    generate_audio(current_card["English"], model, filename)
    play_audio(filename)

def is_known():
    to_learn.remove(current_card)
    new_dict = pd.DataFrame.from_dict(to_learn)
    new_dict.to_csv("data/words_to_learn.csv", index=False)
    next_card()

def next_card():
    global current_card, flip_timer
    current_card = random.choice(to_learn)
    selected_card = current_card["German"]
    window.after_cancel(flip_timer)
    canvas.itemconfig(card_title, text="German", fill="black")
    canvas.itemconfig(card_word, text=selected_card, fill="black")
    canvas.itemconfig(card_side, image=card_front_img)
    window.after(100)
    german_tts()
    flip_timer = window.after(3000, func=flip_card)


def flip_card():

    selected_card = current_card["English"]
    canvas.itemconfig(card_side, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=selected_card, fill="white")
    english_tts()

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_side = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 40, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_button = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_button, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()