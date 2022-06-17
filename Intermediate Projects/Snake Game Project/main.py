# noinspection PySingleQuotedDocstring
'''
Created by: Antonia Andreou
Created Date: 30th March 2022
Amended By: Antonia Andreou
Amended Date: 17th June 2022
'''

# Modules
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time


def controls():
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")


# Settings
screen = Screen()
screen.title("Antonia's Snake Game")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

# Object creation
snake = Snake()
food = Food()
score_board = ScoreBoard()

# MAIN
game_on = True
while game_on:

    # Initiate game
    controls()
    screen.update()
    time.sleep(0.1)
    snake.snake_move()
    score_board.scoreboard_initialization()

    # Detection of food & snake growth
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.snake_extend()
        score_board.score_tracking()
        score_board.highscore_tracking()

    # Score update
    score_board.score_increase()

    # Detection of wall collision
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        # Pop up prompt
        player_continue = screen.textinput("Would you like to play again?", "(y/n)").lower()
        if player_continue == 'y':
            controls()
            score_board.scoreboard_reset()
            snake.snake_reset()
        else:
            score_board.game_over()
            game_on = False

    # Detection of own body collision
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # Pop up prompt
            player_continue = screen.textinput("Would you like to play again?", "(y/n)").lower()
            if player_continue == 'y':
                controls()
                score_board.scoreboard_reset()
                snake.snake_reset()
            else:
                score_board.game_over()
                game_on = False


screen.exitonclick()
