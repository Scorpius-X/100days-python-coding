from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("Pong")
scoreboard = Scoreboard() 
screen.tracer(0)

pong = Ball()
rpaddle = Paddle((350, 0))
lpaddle = Paddle((-350, 0))

screen.listen()
screen.onkey(rpaddle.move_up, "Up")
screen.onkey(rpaddle.move_down, "Down")
screen.onkey(lpaddle.move_up, "w")
screen.onkey(lpaddle.move_down, "s")


game_is_on = True


while game_is_on:
    screen.update()
    time.sleep(pong.move_speed)
    pong.move()
    


    #detect collision with rpaddle wall
    if pong.xcor() > 350:
        pong.reset_position()
        scoreboard.l_point()

    
    #detect collision with lpaddle wall
    if pong.xcor() < -350:
        pong.reset_position()
        scoreboard.r_point()
    

    #detect collision with top and bottom wall
    if pong.ycor() > 280 or pong.ycor() < -280:
        #bounce after collision with wall
        pong.bounce_y()
    
    #detect collision with paddle
    if pong.distance(rpaddle) < 50 and pong.xcor() > 320 or pong.distance(lpaddle) < 50 and pong.xcor() < -320:
        pong.bounce_x()








screen.exitonclick()