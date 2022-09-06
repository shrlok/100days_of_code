class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.right_answer = 0
        self.question_list = q_list

    def still_have_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def next_qestion(self):
        current_question = self.question_list[self.question_number]

        self.question_number += 1
        #for test
        print({current_question.answer})
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Yoy got it! Right!")
            self.right_answer += 1
        else:
            print("That's wrong!")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your correct score is {self.right_answer}/{self.question_number}")

