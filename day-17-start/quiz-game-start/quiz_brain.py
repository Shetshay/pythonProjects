#from main import question_bank
class QuizBrain:
    def __init__(self, question_list):
        self.q_list = question_list
        self.question_number = 0

    def NextQuestion(self):
        current_question = self.q_list[self.question_number]
        self.question_number += 1
        input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")

    def still_has_questions(self):
        #print(len(self.q_list))
        #print(self.question_number)
        return len(self.q_list) > self.question_number

#QuizBrain(question_bank).NextQuestion()

