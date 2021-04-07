from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for i in range(0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230, y=y_positions[i])
    all_turtles.append(new_turtle)



if user_bet:
    is_race_on = True

while is_race_on:
    for new_turtle in all_turtles:
        if new_turtle.xcor() > 230:
            is_race_on = False
            winning_color = new_turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won. The {winning_color} turtle is the winner")
            else:
                print(f"You lost. The {winning_color} turtle won.")
        rand_distance = random.randint(0, 11)
        new_turtle.forward(rand_distance)


screen.exitonclick()