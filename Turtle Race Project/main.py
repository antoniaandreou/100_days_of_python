from turtle import Turtle, Screen
import random


def turtle_racers(color: str, y_pos: int) -> object:
    turtle_racer = Turtle(shape="turtle")
    turtle_racer.color(color)
    turtle_racer.penup()
    turtle_racer.setposition(x=-240, y=y_pos)
    return turtle_racer


def turtle_speed(t_racer: object):
    random_speed = random.randint(1, 9)
    t_racer.speed(random_speed)
    random_move = random.randint(1, 4)
    t_racer.forward(random_move)


# Settings
s = Screen()
s.setup(width=500, height=400)
s.title("Welcome to the Turtle Races!")
t = Turtle()
t.hideturtle()
t.penup()
t.setposition(x=210, y=-190)
t.pendown()
t.setheading(90)
t.forward(400)

# User Choice
user_choice = s.textinput(title="Choose a turtle", prompt="(Red, Blue, Green, Orange, Cyan, Pink)").lower()

# List of Colours
turtle_colours = ["red", "blue", "green", "orange", "cyan", "pink"]

# Increment
distance = [-150, -90, -30, 30, 90, 150]

# Turtle Racers
turtle_objects = []
for c, d in zip(turtle_colours, distance):
    turtle_objects.append(turtle_racers(c, d))

# Main Race
is_race_on = False

if user_choice:
    is_race_on = True

while is_race_on:
    for turtle in turtle_objects:
        turtle_speed(turtle)
        if turtle.xcor() == 210:
            is_race_on = False
            winner = turtle.pencolor()
            if user_choice == winner:
                print(f'You have won! {winner.title()} turtle won the race.')
            else:
                print(f'{user_choice.title()} turtle has lost! The winner was {winner.title()} turtle.')

s.exitonclick()
