from turtle import Turtle, Screen

# Functions


def move_forwards():
    t.forward(10)


def move_backwards():
    t.backward(10)


def turn_right():
    t.right(10)


def turn_left():
    t.left(10)


def clear_reposotion():
    t.penup()
    t.clear()
    t.setposition(0.00, 0.00)
    t.seth(0)
    t.pendown()


# Settings
t = Turtle()
s = Screen()
s.listen()
t.color("DeepPink4")
t.shape("turtle")


# Actions
s.onkey(key="w", fun=move_forwards)
s.onkey(key="s", fun=move_backwards)
s.onkey(key="a", fun=turn_left)
s.onkey(key="d", fun=turn_right)
s.onkey(key="c", fun=clear_reposotion)


s.exitonclick()
