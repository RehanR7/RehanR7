from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9deacon"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = ""
remaining_time = 0

# ---------------------------- WINDOWS FOCUS ------------------------------- #
def focus_window(option):
    if option == "on":
        window.deiconify()
        window.focus_force()
        window.attributes('-topmost', 1)
    elif option == "off":
        window.attributes('-topmost', 0)
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    reps =0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"00:00")
    status_label.config(text="Timer", fg=GREEN)
    focus_window("off")

# ---------------------------- TIMER PAUSED ------------------------------- #
def pause_timer():
    window.after_cancel(timer)
def resume_timer():
    count_down(remaining_time)
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        status_label.config(text="Break", fg=RED)
        focus_window("on")
    elif reps % 2 == 0:
        count_down(short_break_sec)
        status_label.config(text="Break", fg=PINK)
        focus_window("on")
    else:
        count_down(work_sec)
        status_label.config(text="Work")
        focus_window("off")
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global remaining_time
    remaining_time = count
    print(remaining_time)
    count_minutes = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    canvas.itemconfig(timer_text, text= f"{count_minutes}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000,count_down, count -1)
    else:
        start_timer()
        marks = ""
        session_completed = math.floor(reps/2)
        for _ in range(session_completed):
            marks += "✔"
        check_mark.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady= 50, bg=YELLOW)

# Canvas
canvas = Canvas(width=220, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(110, 112, image=tomato_image)
timer_text = canvas.create_text(110, 135, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=2)

# Label
status_label = Label(text="Timer", font=(FONT_NAME, 40, "normal"), fg=GREEN, bg=YELLOW)
status_label.grid(row=1, column=2)

check_mark = Label(fg=GREEN, bg=YELLOW, pady=20, font=(FONT_NAME, 20, "bold"))
check_mark.grid(row=3, column=2)

# Button
start_button = Button(text="Start", font=(FONT_NAME, 12, "bold"), bg=RED, fg="white",
                      command=start_timer, width=10)
start_button.grid(row=4, column=1, pady=10)

pause_button = Button(text="Pause", font=(FONT_NAME, 12, "bold"), bg=GREEN, fg="white",
                      command=pause_timer, width=10)
pause_button.grid(row=4, column=2, pady=10)

resume_button = Button(text="Resume", font=(FONT_NAME, 12, "bold"), bg=GREEN, fg="white",
                      command=resume_timer, width=10)
resume_button.grid(row=5, column=2)

reset_button = Button(text="Reset", font=(FONT_NAME, 12, "bold"), bg=RED, fg="white",
                      command=reset_timer, width=10)
reset_button.grid(row=4, column=3, pady=10)

# Main Loop
window.mainloop()