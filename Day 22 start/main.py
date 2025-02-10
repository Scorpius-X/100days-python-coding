from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("Pong")
screen.tracer(0)
screen.listen()

rpaddle = Paddle((350, 0))
lpaddle = Paddle((-350, 0))
screen.listen()


game_is_on = True


while game_is_on:
    screen.update()
    screen.onkey(rpaddle.move_up, "Up")
    screen.onkey(rpaddle.move_down, "Down")
    screen.onkey(lpaddle.move_up, "w")
    screen.onkey(lpaddle.move_down, "s")


    
    






screen.exitonclick()