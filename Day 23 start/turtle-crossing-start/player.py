STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.restart_line_up()

    def move_turtle(self):
        self.fd(MOVE_DISTANCE)
    
    def restart_line_up(self):
        self.goto(STARTING_POSITION)

    def successful_crossing(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

