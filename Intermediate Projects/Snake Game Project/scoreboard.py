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

    current_score : int
        To pass the current score for the game.
    high_score: int
        To pass and track the highest score achieved.

    Methods
    -------
    scoreboard_initialization:
        Creates the scoreboard object.
    score_tracking:
        Tracks the current score.
    highscore_tracking:
        Keeps record of the highest score achieved.
    score_increase:
        Refreshes the score on display.
    scoreboard_reset:
        Clears the current score and re-initiates the scoreboard object.
    game_over:
        Displays a message when the game has finished.
    """

    def __init__(self):
        """
        Constructs the scoreboard display for a game.
        """
        super().__init__()
        self.current_score = 0
        with open('data.txt') as highscore:
            self.high_score = highscore.read()

    def scoreboard_initialization(self):
        """
        Creates the scoreboard object for the game.
        :return: None
        """
        self.penup()
        self.color(COLOUR)
        self.hideturtle()
        self.goto(X_COORDINATE, Y_COORDINATE)

    def score_tracking(self):
        """
        Tracks the current score for the game.
        :return: None
        """
        self.current_score += 1

    def highscore_tracking(self):
        """
        Keeps track of the highest score achieved in the game.
        :return: None
        """
        if self.current_score > int(self.high_score):
            self.high_score = self.current_score
            with open('data.txt', mode='w') as highscore_data:
                highscore_data.write(str(self.high_score))

    def score_increase(self):
        """
        Clears the screen and displays the score and high score variables passed in the write function.
        :return: None
        """
        self.clear()
        self.write(arg=f"Score: {self.current_score} Highscore: {self.high_score}"
                   , move=False, align=ALIGNMENT, font=FONT)

    def scoreboard_reset(self):
        """
        Clears current score and re-initiates the scoreboard for a game restart.
        :return:
        """
        self.clear()
        self.scoreboard_initialization()
        self.highscore_tracking()
        self.current_score = 0
        self.score_increase()

    def game_over(self):
        """
        Displays the message of Game Over once the game has finished.
        :return: None
        """
        self.goto(0, 0)
        self.write(arg="GAME... OVERRRRRRRR.", move=False, align=ALIGNMENT, font=FONT)
