# noinspection PySingleQuotedDocstring
'''
Created by: Antonia Andreou
Created Date: 21st April 2022
Amended By: Antonia Andreou
Amended Date: 27th April 2022
'''

from turtle import Turtle
import random

COLORS = ["red", "salmon", "gold", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    """
    Class controlling the creation and behaviour of the cars.
    ...
    Methods
    -------
    car_creation:
        creates the car objects stored in a list
    move_car:
        moves the cars across the screen
    speed_up:
        increases the car speed by a specific increment
    """

    def __init__(self):
        self.car_list = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def car_creation(self):
        """
        Creates a car object at random intervals and appends them in a list
        :return: None
        """
        car_interval = random.randint(1, 6)
        if car_interval == 1:
            new_car = Turtle("square")
            new_car.setheading(180)
            new_car.turtlesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.setx(260)
            new_car.sety(random.randint(-250, 250))
            self.car_list.append(new_car)

    def move_car(self):
        """
        Iterates through the car objects and moves them forward by a specifies increment.
        :return: None
        """
        for car in self.car_list:
            car.forward(self.car_speed)

    def speed_up(self):
        """
        Increases the car speed variable by a specified increment
        :return: None
        """
        self.car_speed += MOVE_INCREMENT
