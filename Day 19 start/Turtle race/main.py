from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width= 500, height= 400)

user_bet = screen.textinput(title= "Make a Bet", prompt= "Which turtle wins the race?, enter your color :  ")
race_is_on = False
y_positions = [-150, -100, -50, 0, 50, 100]
color = ["red", "black", "green", "purple", "indigo", "pink"]
all_turtles = []

for turtle_index in  range(0, 6):
    new_turtle = Turtle(shape= "turtle")
    new_turtle.penup()
    new_turtle.color(color[turtle_index])
    new_turtle.goto(x= -220, y = y_positions[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    race_is_on = True

while race_is_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_is_on = False
            winning_turtle = turtle.pencolor()
            if user_bet == winning_turtle:
                print(f"You won the bet!, {winning_turtle} colored turtle is the winner of the race")
            else:
                print(f"You lost the bet!, {winning_turtle} colored turtle is the winner of the race")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)



screen.exitonclick()
