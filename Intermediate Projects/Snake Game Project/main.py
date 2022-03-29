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

    # Detection of food & snake growth
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.snake_extend()
        score += 1

    # Score update
    score_board.score_increase(score=score)

    # Detection of wall collision
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_on = False
        score_board.game_over()

    # Detection of own body collision
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_on = False
            score_board.game_over()

screen.exitonclick()
