from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(20)


def move_backwards():
    tim.backward(20)


def right():
    tim.right(10)


def left():
    tim.left(10)


def reset():
    tim.reset()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=right)
screen.onkey(key="d", fun=left)
screen.onkey(key="c", fun=reset)



screen.exitonclick()