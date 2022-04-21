# noinspection PySingleQuotedDocstring
'''
Created by: Antonia Andreou
Created Date: 2nd April 2022
Amended By: Antonia Andreou
Amended Date: 13th April 2022
'''

from turtle import Turtle

# Class Constants
X_MOVE_DISTANCE = 10
Y_MOVE_DISTANCE = 10
STARTING_SPEED = 0.1


class Ball(Turtle):
    """
    The class controls the ball functions.
    ...
    Attributes
    ----------
    y_move : int
        The number of pixels to move on the y coordinate

    x_move : int
        The number of pixels to move on the x coordinate

    movement_speed : int
        The speed of which the balls moves

    Methods
    -------
    move :
        Moves the ball to a new position

    y_bounce :
        Moves the ball in the opposite y coordinate direction

    x_bounce :
        Moves the ball in the opposite x coordinate direction

    reset_ball :
        Moves ball back in the centre once it gets out of bounds and starts moving it in the opposite direction
    """

    def __init__(self):
        """
        Creates the ball object
        """
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color('white')
        self.x_move = X_MOVE_DISTANCE
        self.y_move = Y_MOVE_DISTANCE
        self.movement_speed = STARTING_SPEED

    def move(self):
        """
        Moves the ball object to new coordinates by a distance specified
        :return: None
        """
        new_x_cor = self.xcor() + self.x_move
        new_y_cor = self.ycor() + self.y_move
        self.goto(new_x_cor, new_y_cor)

    def y_bounce(self):
        """
        Multiplies the y coordinate by -1 to change its direction
        :return: None
        """
        self.y_move *= -1

    def x_bounce(self):
        """
        Multiplies the x coordinate by -1 to change its direction
        :return: None
        """
        self.x_move *= -1
        self.movement_speed *= 0.5

    def reset_ball(self):
        """
        Moves the ball to the centre and changes the x coordinates dorection
        :return: None
        """
        self.goto(0, 0)
        self.movement_speed = STARTING_SPEED
        self.x_bounce()
