from tkinter import *
from tkinter import ttk
import math
from pygame import mixer

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
paused = False
remaining_time = 0
current_total_seconds = 0


# ---------------------------- WINDOW MANAGEMENT ------------------------------- #
def focus_window(option):
    if option == "on":
        window.deiconify()
        window.focus_force()
        window.attributes('-topmost', 1)
    elif option == "off":
        window.attributes('-topmost', 0)


# ---------------------------- SOUND NOTIFICATION ------------------------------- #
def play_sound():
    mixer.init()
    mixer.music.load("alarm.mp3")
    mixer.music.play()  # Frequency: 1000Hz, Duration: 500ms

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps, paused
    reps = 0
    paused = False
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    status_label.config(text="Timer", fg=GREEN)
    check_mark.config(text="")
    session_label.config(text="Work Sessions: 0")
    progress['value'] = 0
    start_button.config(state=NORMAL)
    pause_button.config(state=DISABLED, text="Pause")
    focus_window("off")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps, current_total_seconds
    start_button.config(state=DISABLED)
    pause_button.config(state=NORMAL)

    # Validate and update time entries
    try:
        work_min = max(1, int(work_entry.get()))
    except:
        work_min = WORK_MIN
        work_entry.delete(0, END)
        work_entry.insert(0, WORK_MIN)

    try:
        short_break_min = max(1, int(short_break_entry.get()))
    except:
        short_break_min = SHORT_BREAK_MIN
        short_break_entry.delete(0, END)
        short_break_entry.insert(0, SHORT_BREAK_MIN)

    try:
        long_break_min = max(1, int(long_break_entry.get()))
    except:
        long_break_min = LONG_BREAK_MIN
        long_break_entry.delete(0, END)
        long_break_entry.insert(0, LONG_BREAK_MIN)

    reps += 1
    work_sec = work_min * 60
    short_break_sec = short_break_min * 60
    long_break_sec = long_break_min * 60

    if reps % 8 == 0:
        current_total_seconds = long_break_sec
        count_down(long_break_sec)
        status_label.config(text="Long Break", fg=RED)
        focus_window("on")
    elif reps % 2 == 0:
        current_total_seconds = short_break_sec
        count_down(short_break_sec)
        status_label.config(text="Short Break", fg=PINK)
        focus_window("on")
    else:
        current_total_seconds = work_sec
        count_down(work_sec)
        status_label.config(text="Work", fg=GREEN)
        focus_window("off")

    progress['maximum'] = current_total_seconds
    session_label.config(text=f"Work Sessions: {(reps + 1) // 2}")


# ---------------------------- PAUSE MECHANISM ------------------------------- #
def pause_timer():
    global paused, timer, remaining_time
    if not paused:
        if timer is not None:
            window.after_cancel(timer)
            timer = None
            paused = True
            pause_button.config(text="Resume")
    else:
        paused = False
        pause_button.config(text="Pause")
        count_down(remaining_time)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer, remaining_time
    remaining_time = count

    count_min = math.floor(count / 60)
    count_sec = count % 60
    canvas.itemconfig(timer_text, text=f"{count_min:02d}:{count_sec:02d}")

    progress['value'] = current_total_seconds - count

    if count > 0 and not paused:
        timer = window.after(1000, count_down, count - 1)
    elif count == 0 and not paused:
        play_sound()
        start_timer()
        marks = "✔" * (reps // 2)
        check_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Enhanced Pomodoro Timer")
window.config(padx=30, pady=30, bg=YELLOW)

# Settings Frame
settings_frame = Frame(window, bg=YELLOW)
settings_frame.grid(row=0, column=1, columnspan=3, pady=10)

Label(settings_frame, text="Work (min):", bg=YELLOW, fg=GREEN,
      font=(FONT_NAME, 10)).grid(row=0, column=0, padx=5)
work_entry = Entry(settings_frame, width=5, font=(FONT_NAME, 10))
work_entry.grid(row=0, column=1, padx=5)
work_entry.insert(0, "25")

Label(settings_frame, text="Short Break (min):", bg=YELLOW, fg=PINK,
      font=(FONT_NAME, 10)).grid(row=0, column=2, padx=5)
short_break_entry = Entry(settings_frame, width=5, font=(FONT_NAME, 10))
short_break_entry.grid(row=0, column=3, padx=5)
short_break_entry.insert(0, "5")

Label(settings_frame, text="Long Break (min):", bg=YELLOW, fg=RED,
      font=(FONT_NAME, 10)).grid(row=0, column=4, padx=5)
long_break_entry = Entry(settings_frame, width=5, font=(FONT_NAME, 10))
long_break_entry.grid(row=0, column=5, padx=5)
long_break_entry.insert(0, "20")

# Timer Display
status_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
status_label.grid(row=1, column=1, columnspan=3, pady=10)

canvas = Canvas(width=220, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(110, 112, image=tomato_img)
timer_text = canvas.create_text(110, 140, text="00:00", fill="white",
                                font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=1, columnspan=3)

# Progress Bar
progress = ttk.Progressbar(window, orient=HORIZONTAL, length=400, mode='determinate')
progress.grid(row=3, column=1, columnspan=3, pady=10)

# Controls
start_button = Button(text="Start", font=(FONT_NAME, 12, "bold"), bg=GREEN, fg="white",
                      command=start_timer, width=10)
start_button.grid(row=4, column=1, pady=10)

pause_button = Button(text="Pause", font=(FONT_NAME, 12, "bold"), bg=PINK, fg="white",
                      command=pause_timer, width=10, state=DISABLED)
pause_button.grid(row=4, column=2, pady=10)

reset_button = Button(text="Reset", font=(FONT_NAME, 12, "bold"), bg=RED, fg="white",
                      command=reset_timer, width=10)
reset_button.grid(row=4, column=3, pady=10)

# Session Tracking
session_label = Label(text="Work Sessions: 0", font=(FONT_NAME, 14), bg=YELLOW, fg=GREEN)
session_label.grid(row=5, column=1, columnspan=3, pady=10)

check_mark = Label(font=(FONT_NAME, 24), bg=YELLOW, fg=GREEN)
check_mark.grid(row=6, column=1, columnspan=3)

# Keyboard Shortcuts
window.bind('<Return>', lambda event: start_timer())
window.bind('<space>', lambda event: pause_timer())
window.bind('<Escape>', lambda event: reset_timer())

window.mainloop()