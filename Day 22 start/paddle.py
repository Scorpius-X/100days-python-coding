from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len= 1, stretch_wid= 5)
        self.color("white")
        self.penup()
        self.goto(position)

    def move_up(self):
        current_x = self.xcor()
        new_y = self.ycor() + 20
        self.goto(current_x, new_y)
    

    def move_down(self):
        current_x = self.xcor()
        new_y = self.ycor() - 20
        self.goto(current_x, new_y)