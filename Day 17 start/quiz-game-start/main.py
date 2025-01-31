from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for questions in question_data:
    question_text = questions["question"]
    question_answer = questions["correct_answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(q_list= question_bank)
quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()

print("Congrats, you've completed the quiz game.")
print(f"Your final score is {quiz.score}/{quiz.question_number}")