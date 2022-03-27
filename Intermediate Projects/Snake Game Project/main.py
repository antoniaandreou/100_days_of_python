from turtle import Screen
import time
from snake import Snake
from food import Food

# Settings
screen = Screen()
screen.title("Antonia's Snake Game")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()

print(food.x_coordinate)
print(food.y_coordinate)


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.snake_move()

screen.exitonclick()
