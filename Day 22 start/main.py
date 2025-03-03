from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("Pong")
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
    time.sleep(0.1)
    pong.move()
    


    #detect collision with rpaddle wall
    if pong.xcor() > 350:
        pong.reset_position()
    
    if pong.xcor() < -350:
        pong.reset_position()
    

    #detect collision with top and bottom wall
    if pong.ycor() > 280 or pong.ycor() < -280:
        #bounce after collision with wall
        pong.bounce_y()
    
    #detect collision with paddle
    if pong.distance(rpaddle) < 50 and pong.xcor() > 320 or pong.distance(lpaddle) < 50 and pong.xcor() < -320:
        pong.bounce_x()








screen.exitonclick()