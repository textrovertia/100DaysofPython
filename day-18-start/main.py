from turtle import Turtle, Screen
import random as r

tim = Turtle()
tim.shape("turtle")
tim.color("orange")
tim.pencolor("blue")

# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# for _ in range(50):
#     tim.forward(10)
#     tim.up()
#     tim.forward(10)
#     tim.down()


# for j in range(3, 11):
#     total = 360
#     angle = total/j
#     tim.pencolor(randint(0 , 25), randint(0, 25), randint(0,25))
#     for i in range(j):
#         tim.forward(100)
#         tim.right(angle)

colors = ['blue', 'red', 'orange', 'purple', 'pink', 'green', 'yellow', 'brown', 'gold']
directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")


def random_walk():
    tim.pencolor(r.choice(colors))
    tim.forward(50)
    tim.setheading(r.choice(directions))


# for i in range(0, 100):
#    random_walk()


def random_color():
    red = r.randint(0, 255)
    blue = r.randint(0, 255)
    green = r.randint(0, 255)

    color = (red, blue, green)


tim.color(random_color())
tim.circle(100)







screen = Screen()
screen.exitonclick()