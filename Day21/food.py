from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len= 0.5, stretch_wid= 0.5)
        self.color("white")
        self.speed("fastest")
        new_x = random.randint(-260, 240)
        new_y = random.randint(-260, 240)
        self.goto(new_x,new_y)
        self.refresh()

    def refresh(self):
        new_x = random.randint(-260, 240)
        new_y = random.randint(-260, 240)
        self.goto(new_x,new_y)
