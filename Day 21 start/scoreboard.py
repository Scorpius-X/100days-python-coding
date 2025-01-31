from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

#scoreboard class inherits properties from the turtle class, attributes and methods
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.update_scoreboard()
        

    def update_scoreboard(self):
        self.write(f"score: {self.score}", move= False, align= ALIGNMENT , font= FONT )

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", move= False, align= ALIGNMENT , font= FONT )


        
    #increase the score after each food collision
    def increase(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

