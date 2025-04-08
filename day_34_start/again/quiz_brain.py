
class Brain:
    def __init__(self, question_list):
        self.question_no = 0
        self.questions = question_list
        self.current_question = ""
        self.score = 0
        self.total_questions = len(question_list)
        self.question = ''

    def checking_remaining_question(self):
        if self.question_no < self.total_questions:
            return True

    def next_question(self):
        self.current_question = self.questions[self.question_no]
        self.question_no += 1
        self.question = self.current_question.q_text
        return self.question


    def check_answer(self, user_input):
        answer = self.current_question.q_answer
        if answer == user_input:
            self.score += 1
            print("correct")
            return True
        else:
            print("wrong")
            return False
