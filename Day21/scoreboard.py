from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

#scoreboard class inherits properties from the turtle class, attributes and methods
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.update_scoreboard()
        

    def update_scoreboard(self):
        self.clear()
        self.write(f"score: {self.score} highscore: {self.highscore}", move= False, align= ALIGNMENT , font= FONT )

    
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode= "w") as file:
                file.write(f"{self.highscore}")
    
        self.score = 0
        self.update_scoreboard()

        
    #increase the score after each food collision
    def increase(self):
        self.score += 1
        self.update_scoreboard()

