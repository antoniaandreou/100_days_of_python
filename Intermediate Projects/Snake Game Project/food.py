from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.clear()
        x_coordinate = random.randint(-280, 280)
        y_coordinate = random.randint(-280, 280)
        self.goto(x=x_coordinate, y=y_coordinate)
        self.dot(10, "yellow")


