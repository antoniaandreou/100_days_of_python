# noinspection PySingleQuotedDocstring
'''
Created by: Antonia Andreou
Created Date: 21st April 2022
Amended By: Antonia Andreou
Amended Date: 27th April 2022
'''
from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """
    Class controlling the scoreboard
    ...
    Methods
    -------
    level_display:
        Creates the current level of the game
    game_over:
        Creates the game over display for the game
    """

    def __init__(self):
        super(Scoreboard, self).__init__()
        self.hideturtle()

    def level_display(self, level: int):
        """
        The function displays the number passed in the level parameter when called
        :param level: Integer of the current level
        :return: None
        """
        self.clear()
        self.hideturtle()
        self.penup()
        self.setposition(x=-270, y=270)
        self.write(f"Level: {level}", align="left", font=FONT)

    def game_over(self):
        """
        The function displays the message game over when called
        :return: None
        """
        self.penup()
        self.hideturtle()
        self.setposition(x=0, y=0)
        self.write("GAME OVER", align="center", font=FONT)
