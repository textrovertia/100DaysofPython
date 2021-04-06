from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []

for i in question_data:
    text = i["question"]
    answer = i["correct_answer"]
    new_q = Question(text, answer)
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
else:
    print(f"You've completed the quiz! Your final score is {quiz.score}/12")
