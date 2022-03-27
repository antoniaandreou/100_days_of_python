from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 280)
        self.score_increase(score=0)

    def score_increase(self, score):
        self.clear()
        self.write(arg=f"Score: {score}", move=False, align="center", font=("Arial", 16, "bold"))
