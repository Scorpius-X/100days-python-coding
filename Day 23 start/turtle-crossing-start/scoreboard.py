FONT = ("Courier", 24, "normal")
from turtle import Turtle



class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.score = 1
        self.goto(-280, 250)
        self.update_scoreboard()
        

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.score}", move= False, align= "left", font = FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", move= False, align= "center" , font= FONT )

    def update_level(self):
        self.score += 1
        self.update_scoreboard()

        

