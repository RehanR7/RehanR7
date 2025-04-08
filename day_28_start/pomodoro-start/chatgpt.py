from tkinter import *
import math
import time
from pygame import mixer

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
DARK_BG = "#333"
DARK_TEXT = "#ddd"
FONT_NAME = "Courier"
DEFAULT_WORK_MIN = 25
DEFAULT_SHORT_BREAK_MIN = 5
DEFAULT_LONG_BREAK_MIN = 20
reps = 0
timer = None
paused = False
remaining_time = 0

# Beep sound when a session ends
def play_sound():
    mixer.init()
    mixer.music.load("alarm.mp3")
    mixer.music.play()


def focus_window(option):
    if option == "on":
        window.deiconify()
        window.focus_force()
        window.attributes('-topmost', 1)
    elif option == "off":
        window.attributes('-topmost', 0)


def reset_timer():
    global reps, paused, remaining_time
    reps = 0
    paused = False
    remaining_time = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"00:00")
    status_label.config(text="Timer", fg=GREEN)
    check_mark.config(text="")
    start_button.config(state=NORMAL)
    progress_bar['value'] = 0
    focus_window("off")


def start_timer():
    global reps, paused
    paused = False
    reps += 1

    work_sec = int(work_input.get()) * 60
    short_break_sec = int(short_break_input.get()) * 60
    long_break_sec = int(long_break_input.get()) * 60

    start_button.config(state=DISABLED)

    if reps % 8 == 0:
        count_down(long_break_sec)
        status_label.config(text="Long Break", fg=RED)
        focus_window("on")
    elif reps % 2 == 0:
        count_down(short_break_sec)
        status_label.config(text="Break", fg=PINK)
        focus_window("on")
    else:
        count_down(work_sec)
        status_label.config(text="Work", fg=GREEN)
        focus_window("off")


def count_down(count):
    global timer, remaining_time, paused

    if paused:
        return

    remaining_time = count
    count_minutes = math.floor(count / 60)
    count_seconds = count % 60
    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds:02}")

    progress_bar["value"] = ((DEFAULT_WORK_MIN * 60 - count) / (DEFAULT_WORK_MIN * 60)) * 100

    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        play_sound()
        start_timer()
        marks = "✔" * (reps // 2)
        check_mark.config(text=marks)
        start_button.config(state=NORMAL)


def pause_resume_timer():
    global paused
    if not paused:
        paused = True
        window.after_cancel(timer)
        pause_button.config(text="Resume")
    else:
        paused = False
        count_down(remaining_time)
        pause_button.config(text="Pause")


def toggle_theme():
    current_bg = window.cget("bg")
    if current_bg == YELLOW:
        window.config(bg=DARK_BG)
        canvas.config(bg=DARK_BG)
        status_label.config(bg=DARK_BG, fg=DARK_TEXT)
        check_mark.config(bg=DARK_BG, fg=GREEN)
        theme_button.config(text="Light Mode")
    else:
        window.config(bg=YELLOW)
        canvas.config(bg=YELLOW)
        status_label.config(bg=YELLOW, fg=GREEN)
        check_mark.config(bg=YELLOW, fg=GREEN)
        theme_button.config(text="Dark Mode")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=50, pady=30, bg=YELLOW)

canvas = Canvas(width=220, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(110, 112, image=tomato_image)
timer_text = canvas.create_text(110, 135, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=2)

status_label = Label(text="Timer", font=(FONT_NAME, 40, "normal"), fg=GREEN, bg=YELLOW)
status_label.grid(row=1, column=2)

check_mark = Label(fg=GREEN, bg=YELLOW, pady=20, font=(FONT_NAME, 20, "bold"))
check_mark.grid(row=4, column=2)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=5, column=1)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=5, column=3)

pause_button = Button(text="Pause", highlightthickness=0, command=pause_resume_timer)
pause_button.grid(row=5, column=2)

theme_button = Button(text="Dark Mode", highlightthickness=0, command=toggle_theme)
theme_button.grid(row=6, column=2)

# Input Fields for Custom Time
Label(text="Work (min):", font=(FONT_NAME, 12), bg=YELLOW).grid(row=7, column=1)
Label(text="Short Break (min):", font=(FONT_NAME, 12), bg=YELLOW).grid(row=8, column=1)
Label(text="Long Break (min):", font=(FONT_NAME, 12), bg=YELLOW).grid(row=9, column=1)

work_input = Entry(width=5)
work_input.grid(row=7, column=2)
work_input.insert(0, str(DEFAULT_WORK_MIN))

short_break_input = Entry(width=5)
short_break_input.grid(row=8, column=2)
short_break_input.insert(0, str(DEFAULT_SHORT_BREAK_MIN))

long_break_input = Entry(width=5)
long_break_input.grid(row=9, column=2)
long_break_input.insert(0, str(DEFAULT_LONG_BREAK_MIN))

# Progress Bar
from tkinter.ttk import Progressbar

progress_bar = Progressbar(window, orient=HORIZONTAL, length=200, mode='determinate')
progress_bar.grid(row=3, column=2)

window.mainloop()
