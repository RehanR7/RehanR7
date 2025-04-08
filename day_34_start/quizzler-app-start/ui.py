from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.windows = Tk()
        self.windows.title("Quizler")
        self.windows.config(padx=20, pady=20, background=THEME_COLOR)

        self.canvas = Canvas(
            master=self.windows,
            background="white",
            bd=0,
            highlightthickness=0,
            height=250,
            width=300
        )
        self.question_text = self.canvas.create_text(150,125, text="", width=280, font=("Arial", 12, "italic"), fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=5, pady=20)

        self.score_label = Label(text="Score: 0",
                                 pady=30, padx=10,
                                 background=THEME_COLOR,
                                 font=("Arial", 15, "normal"),
                                 fg="white"
                                 )
        self.score_label.grid(row=0, column=1)

        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")
        self.correct_button = Button(master= self.windows,image=true_image, bd=False, highlightthickness=0,
                                     command=self.true_answer_button)
        self.correct_button.grid(row=2, column=1, padx=10, pady=30)
        self.wrong_button = Button(master= self.windows,image=false_image, bd=False, highlightthickness=0,
                                   command=self.false_answer_button)
        self.wrong_button.grid(row=2, column=0, padx=10, pady=30)
        self.next_question()

        self.windows.mainloop()

    def next_question(self):
        self.canvas.config(background="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.score_label.config(text=f"You scored: {self.quiz.score}/{self.quiz.question_number}")
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz!")
            self.correct_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def true_answer_button(self):
        self.feedback(self.quiz.check_answer("True"))

    def false_answer_button(self):
        self.feedback(self.quiz.check_answer("False"))


    def feedback(self, is_right):
        if is_right:
            self.canvas.config(background="green")
        else:
            self.canvas.config(background="red")
        self.windows.after(1000, self.next_question)