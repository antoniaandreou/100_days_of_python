from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

# Settings
screen = Screen()
screen.title("Antonia's Snake Game")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

score = 0
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.snake_move()

    if snake.head.distance(food) < 15:
        food.refresh()
        score += 1

    score_board.score_increase(score=score)

screen.exitonclick()
