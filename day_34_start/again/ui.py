from tkinter import *
from quiz_brain import Brain

class Display:
    def __init__(self, mind: Brain):
        self.brain = mind
        self.windows = Tk()
        self.windows.title("Quiz Game")
        self.windows.config(background="light blue", padx=20, pady=20)

        self.canvas = Canvas(master=self.windows, background="white", height=250, width=300)
        self.canvas.grid(row=1, column=0, columnspan=2)
        self.canvas_text = self.canvas.create_text(150,125, text="", width=280, font=("Arial", 12, "italic"), fill="blue")

        self.score_label = Label(master=self.windows, text=f"Score: 0",background="light blue", font=("Arial", 15, "normal"), pady=10, fg="red")
        self.score_label.grid(row=0, column=1)

        true_img = PhotoImage(file="../quizzler-app-start/images/true.png")
        self.true_button = Button(master=self.windows, highlightthickness=0, image=true_img, command=self.correct_answer)
        self.true_button.grid(row=2, column= 1, padx=10, pady=15)

        false_img = PhotoImage(file="../quizzler-app-start/images/false.png")
        self.false_button = Button(master=self.windows, highlightthickness=0, image=false_img, command=self.wrong_answer)
        self.false_button.grid(row=2, column=0,padx=10, pady=15)

        self.next()

        self.windows.mainloop()

    def next(self):
        self.canvas.config(background="white")
        if self.brain.checking_remaining_question():
            self.score_label.config(text=f"Score: {self.brain.score}")
            q_text = self.brain.next_question()
            self.canvas.itemconfig(self.canvas_text, text=q_text)
        else:
            self.canvas.itemconfig(self.canvas_text, text="You have reached the end of the Quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def correct_answer(self):
        self.feedback(self.brain.check_answer("True"))

    def wrong_answer(self):
        self.feedback(self.brain.check_answer("False"))

    def feedback(self, is_rigth):
        if is_rigth:
            self.canvas.config(background="green")
        else:
            self.canvas.config(background="red")

        self.windows.after(1000, self.next)


