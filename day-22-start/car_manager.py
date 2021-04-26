from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=1.5)
        self.color(random.choice(COLORS))
        self.penup()
        self.x = random.randint(-280, 300)
        self.y = random.randint(-250, 280)
        self.setpos(self.x, self.y)

    #TODO: Get cars to move
    def move(self):
        new_x = self.xcor() - MOVE_INCREMENT
        self.goto(new_x, self.y)
