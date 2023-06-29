import turtle
import pandas as pd

# Function to get the coords from the screen by clicking in it
# def get_mouse_click_coor(x, y):
#     print(x,y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Load CSV Data
df = pd.read_csv("50_states.csv")
state_list = df["state"].to_list()


# Correct answers count
correct_answers = 0
correct_states = []


while correct_answers < 50:
    answer_state = screen.textinput(title=f'{correct_answers}/50 Guess the State',
                                    prompt="What's another state's name?")
    answer_state = answer_state.title()

    if answer_state == "Exit":
        states_to_learn = []
        for item in state_list:
            if item not in correct_states:
                states_to_learn.append(item)
        states_to_learn = pd.DataFrame(states_to_learn)
        states_to_learn.to_csv("states_to_learn.csv")
        break

    if answer_state in state_list and answer_state not in correct_states:
        correct_states.append(answer_state)
        correct_answers += 1
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = df[df.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state, font=('Arial', 9, 'normal'))
    else:
        pass


screen.exitonclick()
