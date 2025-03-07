from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len= 2, stretch_wid= 1)
        self.color(random.choice(COLORS))
        self.penup()
        self.create_cars
    

    def move_cars(self):
        self.backward(STARTING_MOVE_DISTANCE)

    
    def create_cars(self):
        for i in range(6):
            new_pos = random.randint(-180, 180)
            self.goto(500, new_pos)

     

     
    

