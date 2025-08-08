from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    
    def __init__(self, quizbrain: QuizBrain):
        self.quiz = quizbrain
        self.window = Tk()
        self.window.title("QUizzler")
        self.window.config(padx= 20, pady= 20, bg= THEME_COLOR)

        #widgets
        self.scorepoint = Label(text= f"score : 0 ",fg= "white", bg= THEME_COLOR )
        self.scorepoint.grid(row= 0, column= 1)

        #create canvas
        self.canvas = Canvas(width= 300, height= 250, bg= "white")
        self.canvas.grid(row= 1, column= 0, columnspan= 2, pady= 50)
        self.question = self.canvas.create_text(150, 125,text = "Extraordinary", width= 280, font= ("arial", 20, "italic") )
        false_img = PhotoImage(file = "100days-python-coding\\Day34\\images\\false.png")
        true_img = PhotoImage(file = "100days-python-coding\\Day34\\images\\true.png")
        self.right_button = Button(image= true_img, highlightthickness=0, command= self.true_button )
        self.wrong_button = Button(image= false_img, highlightthickness=0, command= self.false_button)

        self.right_button.grid(row=2, column= 0)
        self.wrong_button.grid(row=2, column= 1)

        self.get_next_question()
        
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(background= "white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text = q_text)
            self.scorepoint.config(text= f"score: {self.quiz.score}")
            
        else:
            self.canvas.itemconfig(self.question, text = "you have completed the quiz")
            self.right_button.config(state = "disabled")
            self.wrong_button.config(state = "disabled")

    def true_button(self):
        is_right = self.quiz.check_answer(user_answer= "True")
        self.give_feedback(is_right)

    def false_button(self):
        is_right = self.quiz.check_answer(user_answer= "False")
        self.give_feedback(is_right)

    def give_feedback(self,is_right):
        if is_right == True:
            self.canvas.config(background= "green")
            
        else:
            self.canvas.config(background= "red")
        self.window.after(500, self.get_next_question)
        