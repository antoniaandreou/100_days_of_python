# import colorgram
from turtle import Turtle, Screen
import random

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_colour = (r, g, b)
#     rgb_colors.append(new_colour)
#
# print(rgb_colors)

# 10 x 10 dots, 20 diameter 50 paces apart
colour_list = [
    (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50),
    (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73),
    (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158),
    (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19),
    (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)
]

# Settings

t = Turtle()
s = Screen()
s.colormode(255)
t.penup()
t.hideturtle()
t.setposition(-225, -225)

for y in range(-225, 275, 50):
    t.setposition(-225, y)
    for _ in range(10):
        colour = random.choice(colour_list)
        t.dot(20, colour)
        t.forward(50)

s.exitonclick()
