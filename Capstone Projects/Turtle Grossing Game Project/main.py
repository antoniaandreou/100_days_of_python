# noinspection PySingleQuotedDocstring
'''
Created by: Antonia Andreou
Created Date: 21st April 2022
Amended By: Antonia Andreou
Amended Date: 27th April 2022
'''

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Screen settings
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Antonia's Turtle Crossing")
screen.tracer(0)

player = Player()
score = Scoreboard()
cars = CarManager()

# Player controls
screen.listen()
screen.onkey(player.player_movement, "Up")

game_is_on = True
level = 1

while game_is_on:
    time.sleep(0.1)
    screen.update()
    score.level_display(level)

    # Create a series of cars
    cars.car_creation()
    cars.move_car()

    # Detect safe crossing of turtle
    if player.ycor() >= 280:
        level += 1
        player.player_reset()
        cars.speed_up()

    # Detect collision with a car
    for car in cars.car_list:
        if player.distance(car) < 20:
            score.game_over()
            game_is_on = False

screen.exitonclick()
