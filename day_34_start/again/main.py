from data import question_data
import html
from quiz_brain import Brain
from question_model import Question
from ui import Display

question_list = []
for question in question_data:
    text = html.unescape(question["question"])
    answer = html.unescape(question["correct_answer"])
    Q = Question(text, answer)
    question_list.append(Q)


brian = Brain(question_list)
display = Display(brian)