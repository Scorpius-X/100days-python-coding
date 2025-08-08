from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.bgcolor("black")
screen.screensize(canvheight= 600, canvwidth= 600)
screen.tracer(0)

screen.listen()
snake = Snake()



screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


 


screen.exitonclick()




        
      









