import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game ")
image = "Day25.2\\blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

# code to get the x and y coordinates of the turtle screen
# def get_mouse_onscreenclick_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_onscreenclick_coor)
start_game = True

guessed_states = []

while len(guessed_states) < 50:
    
    guess_state = screen.textinput(title= f"{len(guessed_states)} /50 states correct", prompt= "What's another state's name?")
    answer = guess_state.title()

    data = pandas.read_csv("Day25.2\\50_states.csv")
    matching_state = data[data.state == answer]

    if answer == "Exit":
        not_guessed = [item for item in data.state if item not in guessed_states]
        df = pandas.DataFrame(not_guessed)
        df.to_csv("Day25.2\\states_to_learn.csv", index= False, header= False)
        break

    if not matching_state.empty:
        guessed_states.append(matching_state.state.item())
        match_dict = matching_state.to_dict()
        for index in match_dict["x"]:
            x = match_dict["x"][index]
            y = match_dict["y"][index]
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            t.goto(x,y)
            t.pendown()
            t.write(answer)
    




