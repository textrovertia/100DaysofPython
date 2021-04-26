from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard (Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(-200, 250)
        self.level = 0
        self.update_score()


    def update_score(self):
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def next_level(self):
        self.clear()
        self.level += 1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font= FONT)