# noinspection PySingleQuotedDocstring
'''
Created by: Antonia Andreou
Created Date: 2nd April 2022
Amended By: Antonia Andreou
Amended Date: 13th April 2022
'''
# Modules
from turtle import Turtle

# Class Constants
RIGHT_PADDLE_X_AXIS = 350
LEFT_PADDLE_X_AXIS = -350
HEADING = 90
MOVING_DISTANCE = 20


class Paddles(Turtle):
    """
    A class to represents the paddles in the pong game
    ...
    Attributes
    ----------
    side : str
        side of paddle being created

    Methods
    -------
    paddle_creation:
        creates the left and right paddle
    move_up:
        moves paddle upwards by specified distance
    move_down:
        moves paddle upwards by specified distance
    """

    def __init__(self, side: str):
        """
        The function initiates the paddles
        :param side: A string indicating "left" or "right" paddle to be created
        """
        super().__init__()
        self.side = side
        self.paddle_creation()

    def paddle_creation(self):
        """
        Creates the pong paddles. Located to the left and right of the screen.
        :return: None
        """
        self.hideturtle()
        self.penup()
        self.shape("square")
        self.turtlesize(stretch_wid=1, stretch_len=5)
        self.color("white")
        self.setheading(HEADING)
        if self.side.lower() == "right":
            self.setposition(x=RIGHT_PADDLE_X_AXIS, y=0)
        elif self.side.lower() == "left":
            self.setposition(x=LEFT_PADDLE_X_AXIS, y=0)
        self.showturtle()

    def move_up(self):
        """
        Moves the paddle forward by the number of pixels specified.
        :return: None
        """
        self.forward(MOVING_DISTANCE)

    def move_down(self):
        """
        Moves the paddle backwards by the number of pixels specified.
        :return: None
        """
        self.backward(MOVING_DISTANCE)
