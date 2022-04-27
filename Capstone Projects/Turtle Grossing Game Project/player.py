# noinspection PySingleQuotedDocstring
'''
Created by: Antonia Andreou
Created Date: 21st April 2022
Amended By: Antonia Andreou
Amended Date: 27th April 2022
'''

from turtle import Turtle

# Class Constants
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    """
    Class creates the player objects and its associate controls.
    ...
    Methods
    -------
    player_creation:
        Creates the player object
    player_movement:
        Moves the player object
    player_reset:
        Resets player object to starting position
    """

    def __init__(self):
        super().__init__()
        self.player_creation()

    def player_creation(self):
        """
        Creates the player object and sets it to the starting position
        :return: None
        """
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.setposition(STARTING_POSITION)

    def player_movement(self):
        """
        Moves the player object forward
        :return: None
        """
        self.forward(MOVE_DISTANCE)

    def player_reset(self):
        """
        Clears the screen and re-positions the player object back to the starting position
        :return: None
        """
        self.clear()
        self.setposition(STARTING_POSITION)
