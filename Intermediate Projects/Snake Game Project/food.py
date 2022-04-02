'''
Created by: Antonia Andreou
Created Date: 30th March 2022
Amended By: Antonia Andreou
Amended Date: 2nd April 2022
'''

# Modules
from turtle import Turtle
import random

# Class Constants
SPEED = "fastest"
STARTING_NUMBER = -270
ENDING_NUMBER = 270
SIZE = 10
COLOUR = "yellow"

class Food(Turtle):
    """
    A class to represent the snake food for the game.
    ...
    Attributes
    ----------

    Methods
    -------
    refresh:
        Creates a new random position for the food.
    """

    def __init__(self):
        """
        Constructs the snake food for the game.
        """
        super().__init__()
        self.penup()
        self.hideturtle()
        self.speed(SPEED)
        self.refresh()

    def refresh(self):
        """
        Clears the current food from the screen and displays it again at a new random position.
        :return: None
        """
        self.clear()
        x_coordinate = random.randint(STARTING_NUMBER, ENDING_NUMBER)
        y_coordinate = random.randint(STARTING_NUMBER, ENDING_NUMBER)
        self.goto(x=x_coordinate, y=y_coordinate)
        self.dot(SIZE, COLOUR)
