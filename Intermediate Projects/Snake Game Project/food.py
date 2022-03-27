from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.x_coordinate = random.randint(-280, 280)
        self.y_coordinate = random.randint(-280, 280)
        self.goto(x=self.x_coordinate, y=self.y_coordinate)
        self.dot(10, "yellow")
