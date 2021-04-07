import turtle as t
import random as r

tim = t.Turtle()
tim.shape("turtle")
t.colormode(255)


def random_color():
    red = r.randint(0, 255)
    blue = r.randint(0, 255)
    green = r.randint(0, 255)

    color = (red, blue, green)
    return color


tim.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading()+ size_of_gap)


draw_spirograph(1)

screen = t.Screen()
screen.exitonclick()