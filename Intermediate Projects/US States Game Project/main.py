"""
Created By: Antonia Andreou
Created Date: 24 June 2022
Last Edited By:
Last Edited Date:
"""

import turtle
import pandas as pd

# CONSTANTS
ALIGNMENT = 'center'
FONT = ('Microsoft San Serif', 18, 'bold')


def print_state(state: str, x_cor: int, y_cor: int):
    """
    The function uses the turtle module to write the different states on the image for the given coordinates
    :param state: Name of state to be written
    :param x_cor: The x coordinate for the location
    :param y_cor: The y coordinate for the location
    :return: Stamp of the state at the given coordinates
    """
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.shape("circle")
    t.resizemode(rmode="user")
    t.shapesize(0.2, 0.2)
    t.color('blue')
    t.goto(x_cor, y_cor)
    t.write(state)
    t.showturtle()


# Screen settings
screen = turtle.Screen()
screen.title("Antonia's U.S. States Games")
screen.setup(width=900, height=600)
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

# Read csv into a dataframe
states_by_location = pd.read_csv('50_states.csv')
states = states_by_location["state"].to_list()

# Get the players first guess
player_answer = turtle.textinput(title="Guess a state", prompt="What's another state name?").title()

# Main
score = 0
while len(states) != 0:
    answer_check = states_by_location.loc[states_by_location["state"] == player_answer]

    if player_answer == "Exit":
        break
    if player_answer in states:
        x = int(answer_check["x"])
        y = int(answer_check["y"])
        print_state(player_answer, x_cor=x, y_cor=y)
        states.remove(player_answer)
        score += 1
        player_answer = turtle.textinput(title=f"{score}/50 states found", prompt="What's another state name?").title()
    else:
        player_answer = turtle.textinput(title=f"{score}/50 states found", prompt="What's another state name?").title()

# Output missed states to CSV
state_dict = {'Missed States': states}
df = pd.DataFrame(state_dict)
df.to_csv('Missed States.csv')
