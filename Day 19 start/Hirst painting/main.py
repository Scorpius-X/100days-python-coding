# import colorgram
# colors = colorgram.extract('Day 19 start/Hirst painting/img.jpg', 30)
import turtle as t
import random
t.colormode(255)
tim = t.Turtle()
tim.hideturtle()

color_palette = [(230, 239, 234), (205, 153, 99), (225, 205, 103), (161, 55, 101), (113, 187, 213),
                 (154, 31, 58), (8, 109, 166), (42, 13, 24), (160, 29, 25),
                   (12, 23, 52), (34, 122, 62), (59, 23, 18), (9, 32, 26), (186, 156, 173), (63, 166, 88), (171, 57, 42),
                     (156, 208, 215), (94, 183, 167), (205, 99, 95), (240, 200, 3), (213, 174, 198),
                       (28, 37, 105), (187, 99, 110), (163, 209, 197), (220, 177, 173), (14, 105, 56)]
tim.penup()
endpos = -250

for i in range(10):
    tim.setposition(-250, endpos)
    endpos += 50
    for _ in range(11):
        tim.dot(20, random.choice(color_palette)); tim.fd(50)

screen = t.Screen()
screen.exitonclick()




# for coloring in colors:
#     r = coloring.rgb.r
#     b = coloring.rgb.b
#     g = coloring.rgb.g
#     new_color = (r,g,b)
#     color_palette.append(new_color)

# print(color_palette)
