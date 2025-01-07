import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.hideturtle()
tim.speed("fastest")
directions = [0, 90, 180, 270]

def random_color():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    return (r, g, b)

def set_draw_gap(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.pencolor(random_color())
        tim.setheading(tim.heading() + size_of_gap)
        tim.circle(100)
                 
set_draw_gap(5)


# for _ in range(500):
#     tim.pencolor(random_color())
#     tim.fd(30)
#     tim.setheading(random.choice(directions))




# def move_up():
#     tim.left(90)
#     tim.forward(20)

# def move_down():
#     tim.right(90)
#     tim.forward(20)

# def move_forward():
#     tim.forward(20)

# def move_backward():
#     tim.backward(20)

# moves = [move_up, move_down, move_forward, move_backward]


# for i in range(500):
#     tim.color(random.choice(colors))
#     random.choice(moves)()


# def n_sides(num_sides, sides):
#     for n in range(sides):
#         tim.right(num_sides)
#         tim.forward(100)

# for sides in range(3, 11):
#     tim.color(random.choice(colors))
#     num_sides = 360 / sides
#     n_sides(num_sides, sides)

# tim.color("red")
# for triangle in range(3):
#     tim.right(120)
#     tim.forward(100)

# tim.color("green")
# for square in range(4):
#     tim.right(90)
#     tim.forward(100)

# tim.color("black")
# for pentagon in range(5):
#     tim.right(72)
#     tim.forward(100)

# tim.color("orange")
# for hexagon in range(6):
#     tim.right(60)
#     tim.forward(100)

# tim.color("purple")
# for heptagon in range(7):
#     tim.right(51.4285714)
#     tim.forward(100)

# tim.color("brown")
# for octagon in range(8):
#     tim.right(45)
#     tim.forward(100)

# tim.color("cyan")
# for nonagon in range(9):
#     tim.right(40)
#     tim.forward(100)

# tim.color("teal")
# for decagon in range(10):
#     tim.right(36)
#     tim.forward(100)



screen = t.Screen()
screen.exitonclick()

# for _ in range(3):
#     tim.right(90)
#     tim.forward(100)
# tim.right(90)
# tim.forward(90)

# for _ in range(10):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
