from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_q = Question(question_text, question_answer)
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)
while quiz.still_have_question():
    quiz.next_qestion()

print("You've complited th quiz!")
print(f"You final score is: {quiz.right_answer}/{quiz.question_number} ")