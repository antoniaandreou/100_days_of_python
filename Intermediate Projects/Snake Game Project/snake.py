# noinspection PySingleQuotedDocstring
'''
Created by: Antonia Andreou
Created Date: 30th March 2022
Amended By: Antonia Andreou
Amended Date: 17th June 2022
'''

# Modules
from turtle import Turtle

# Class constants
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """
    A class to represent the snake.
    ...
    Attributes
    ----------
    position : tuple
        the positional coordinates for the snake

    Methods
    -------
    starting_position:
        creates 3 tuples with x & y coordinates for the starting position of the snake
    snake_specs:
        the snake setup parameters
    create_snake:
        use outputs from methods above to create the initial snake
    snake_move:
        makes the snake move forward on screen
    snake_extend:
        increases the elements of the snake by one from its tail
    snake_reset:
        move existing segments off the board, clears them and re-initiates the snake
    up:
        changes the snake heading by 90 degrees
    down:
        changes the snake heading by 270 degrees
    left:
        changes the snake heading by 180 degrees
    right:
        changes the snake heading by 0 degrees
    """

    def __init__(self):
        """
        Constructs the snake objects by calling the create_snake method.
        """
        self.segments = []
        self.positions = []
        self.create_snake()
        self.head = self.segments[0]
        self.tail = self.segments[-1]

    def starting_positions(self):
        """
        Creates the starting positions for the snake objects.
        Tuples with object coordinates saved in positions list part of __init__
        :return: None
        """
        x = 0
        y = 0
        for i in range(0, 3, 1):
            self.positions.append((x, y))
            x = x - 20

    def snake_specs(self, position: tuple):
        """
        Setups the object specifications. Objects saved in segments list part of __init__
        :param position: tuple with object coordinates
        :return: None
        """
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def create_snake(self):
        """
        Creates all snake objects by calling the starting_positions & snake_specs methods.
        :return: None
        """
        self.starting_positions()
        for p in self.positions:
            self.snake_specs(p)

    def snake_move(self):
        """
        Moves each object forward by the MOVE_DISTANCE constant.
        :return: None
        """
        for snk in range(len(self.segments) - 1, 0, -1):
            new_x_coordinate = self.segments[snk - 1].xcor()
            new_y_coordinate = self.segments[snk - 1].ycor()
            self.segments[snk].setposition(new_x_coordinate, new_y_coordinate)
        self.head.forward(MOVE_DISTANCE)

    def snake_extend(self):
        """
        Adds objects add the end of the object snake chain.
        :return: None
        """
        x_coordinate = self.tail.xcor()
        y_coordinate = self.tail.ycor()
        positional_extension = (x_coordinate, y_coordinate)
        self.snake_specs(positional_extension)

    def snake_reset(self):
        """
        Moves existing segments out of the board, clears and re-initiates the snake.
        :return: None
        """
        for seq in self.segments:
            seq.goto(1500, 1500)
        self.segments.clear()
        self.positions.clear()
        self.create_snake()
        self.head = self.segments[0]

    def up(self):
        """
        Sets the first object's heading to 90 degrees.
        :return: None
        """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """
        Sets the first object's heading to 270 degrees.
        :return: None
        """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        """
        Sets the first object's heading to 180 degrees.
        :return: None
        """
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        """
        Sets the first object's heading to 0 degrees.
        :return: None
        """
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
