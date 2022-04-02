# noinspection PySingleQuotedDocstring
'''
Created by: Antonia Andreou
Created Date: 30th March 2022
Amended By: Antonia Andreou
Amended Date: 2nd April 2022
'''

# Modules
from turtle import Turtle

# Class Constants
COLOUR = "white"
X_COORDINATE = 0
Y_COORDINATE = 280
ALIGNMENT = "center"
FONT = ("Courier", 16, "bold")


class ScoreBoard(Turtle):
    """
    A class to represent the scoreboard for a game.
    ...
    Attributes
    ----------

    score : int
        To pass the current score for the game.

    Methods
    -------
    score_increase:
        Refreshes the score on display.
    game_over:
        Displays a message when the game has finished.
    """

    def __init__(self):
        """
        Constructs the scoreboard display for a game.
        """
        super().__init__()
        self.penup()
        self.color(COLOUR)
        self.hideturtle()
        self.goto(X_COORDINATE, Y_COORDINATE)
        self.score_increase(score=0)

    def score_increase(self, score: int):
        """
        Clears the screen and displays the score passed in the function.
        :param score: integer input of current score
        :return: None
        """
        self.clear()
        self.write(arg=f"Score: {score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        """
        Displays the message of Game Over once the game has finished.
        :return: None
        """
        self.goto(0, 0)
        self.write(arg="GAME... OVERRRRRRRR.", move=False, align=ALIGNMENT, font=FONT)
