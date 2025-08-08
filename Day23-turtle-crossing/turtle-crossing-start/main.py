import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
carm = CarManager()


player = Player()
scorebd = Scoreboard()
screen.listen()

screen.onkey(player.move_turtle, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    carm.create_car()
    carm.move_cars()

    #detect when turtle collides with car
    for cars in carm.all_cars:
        if cars.distance(player) < 20:
            game_is_on = False
            scorebd.game_over()



    #detect successful crossing
    if player.successful_crossing():
        player.restart_line_up()
        carm.level_up()
        scorebd.update_level()

screen.exitonclick()