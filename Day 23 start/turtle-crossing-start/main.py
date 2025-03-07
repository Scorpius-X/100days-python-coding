import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
car = CarManager()


player = Player()
score = Scoreboard()
screen.listen()

screen.onkey(player.move_turtle, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.move_cars()

   