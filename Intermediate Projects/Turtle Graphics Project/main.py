from turtle import Turtle, Screen
import random


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, g, b)
    return colour


pointer = Turtle()
screen = Screen()

# Settings
pointer.shape("classic")
screen.colormode(255)
pointer.penup()
pointer.setposition(-50.00, 0.00)
pointer.speed("fastest")

# Movements

pointer.pendown()

for i in range(1, 201, 3):
    pointer.seth(i)
    pointer.left(i)
    pointer.color(random_colour())
    pointer.circle(100)

"""
for i in range(3, 11):
    angle = 360 / i
    pointer.color(random_colour())
    for x in range(i):
        pointer.pendown()
        pointer.forward(70)
        pointer.right(angle)
    for x in range(i):
        pointer.pendown()
        pointer.forward(70)
        pointer.left(angle)


for i in range(1, 100):
    pointer.pendown()

    # Colour settings
    pointer.color(random_colour())

    # Size
    pen_sz = random.randint(5, 7)
    pointer.pensize(pen_sz)

    # Distance
    paces = random.randint(20, 50)
    pointer.forward(paces)

    # Turn direction
    direction = random.choice(['right', 'left'])
    angle = random.randrange(0, 360, 90)
    if direction == 'left':
        pointer.left(angle)
    else:
        pointer.right(angle)
"""


screen.exitonclick()
