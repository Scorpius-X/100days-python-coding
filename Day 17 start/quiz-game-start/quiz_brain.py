# this asks the user questions
#checks if the user is correct 
#checks if we are at the end of the quiz
class QuizBrain: 
    """A Robot Ai that has methods that generates questions in form of text and answers"""

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        """A method that checks if the questions have exceeded the questions in the list"""
        if self.question_number < len(self.question_list):
            return True
        else:
            return False


    def next_question(self): #this is a method (a method gives this code a function)
        """A method that generates a new question and answers from the question bank"""
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text}. (True/false): ")
        self.check_answer(user_answer, current_question.answer)


    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")
