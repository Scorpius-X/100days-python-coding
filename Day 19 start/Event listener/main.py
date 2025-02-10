from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_left():
    tim.left(10)

# def turn_left():
#     new_heading = tim.heading() - 10
#     tim.setheading(new_heading)
def turn_right():
    tim.right(10)

# def turn_right():
#     new_heading = tim.heading() + 10
#     tim.setheading(new_heading)

def clear_drawing():
    tim.home()
    tim.clear()
    

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear_drawing, "c")
screen.exitonclick()