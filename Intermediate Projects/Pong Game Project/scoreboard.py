# noinspection PySingleQuotedDocstring
'''
Created by: Antonia Andreou
Created Date: 2nd April 2022
Amended By: Antonia Andreou
Amended Date: 13th April 2022
'''
from turtle import Turtle

# Class constants
FONT = ('Arial', 24, 'bold')
ALIGNMENT = 'center'
HEIGHT_YCOR = 270
RIGHT_XCOR = 140
LEFT_XCOR = -140


class ScoreBoard(Turtle):
    """
    The class controls the scoreboard
    ...
    Methods
    -------
    score :
        Displays the score for the players
    """

    def __init__(self):
        super(ScoreBoard, self).__init__()

    def score(self, score: int, player_side: str):
        """
        Displays the score passed in the function according to the side defined in 'player_side'.
        :param score: integer passed in the function
        :param player_side: string of either 'left' or 'right' depending on the player
        :return:
        """
        self.color('white')
        self.penup()
        self.hideturtle()
        if player_side.lower() == 'left':
            self.goto(LEFT_XCOR, HEIGHT_YCOR)
        elif player_side.lower() == 'right':
            self.goto(RIGHT_XCOR, HEIGHT_YCOR)
        self.write(arg=score, align=ALIGNMENT, font=FONT)
