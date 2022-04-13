# noinspection PySingleQuotedDocstring
'''
Created by: Antonia Andreou
Created Date: 2nd April 2022
Amended By: Antonia Andreou
Amended Date: 13th April 2022
'''

# Modules
from turtle import Screen
from paddles import Paddles
from ball import Ball
from scoreboard import ScoreBoard
import time

# Settings
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Antonia's PONG")
screen.tracer(0)

# Paddle creation
l_paddle = Paddles("left")
r_paddle = Paddles("right")

# Ball creation
ball = Ball()

# Scorecard creation
score_board = ScoreBoard()

# Allocate keyboard keys to each paddle
screen.listen()
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")

left_score = 0
right_score = 0

game_on = True
while game_on:
    time.sleep(ball.movement_speed)
    screen.update()
    ball.move()
    score_board.score(left_score, 'left')
    score_board.score(right_score, 'right')

    # Detect collision with  width walls
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.y_bounce()

    # Detect collision with paddles
    if ball.xcor() < -320 and ball.distance(l_paddle) < 40 or ball.xcor() > 320 and ball.distance(r_paddle) < 40:
        ball.x_bounce()

    # Detect if ball passes beyond the right bounds
    if ball.xcor() > 380:
        score_board.clear()
        left_score += 1
        time.sleep(0.5)
        ball.reset_ball()

    # Detect if ball passes beyond the left bounds
    if ball.xcor() < -380:
        score_board.clear()
        right_score += 1
        time.sleep(0.5)
        ball.reset_ball()

screen.exitonclick()
