import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


    


player = Player()
score = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    positions = [(250, -150),(250, -100),(250, -50), (250, 0), (250, 50), (250, 100),(250, 150) ]
    for i in range(50):
        for position in random.choice(positions):
            cars = CarManager(position)
        cars.move_cars()