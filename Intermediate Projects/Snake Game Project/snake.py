from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.positions = []
        self.create_snake()
        self.head = self.segments[0]

    def starting_positions(self):
        x = 0
        y = 0
        for i in range(0, 3, 1):
            self.positions.append((x, y))
            x = x - 20

    def create_snake(self):
        self.starting_positions()
        for p in self.positions:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(p)
            self.segments.append(new_segment)

    def snake_move(self):
        for snk in range(len(self.segments) - 1, 0, -1):
            new_x_coordinate = self.segments[snk - 1].xcor()
            new_y_coordinate = self.segments[snk - 1].ycor()
            self.segments[snk].setposition(new_x_coordinate, new_y_coordinate)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
