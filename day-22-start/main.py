from turtle import Screen
from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard
import time

cars = []
print(cars)

# TODO: Create screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# TODO: Create player, cars and scoreboard
player = Player()
scoreboard = Scoreboard()

for car in range (0, 30 ):
    new_car = CarManager()
    cars.append(new_car)

# TODO:Get screen to listen when forward key is clicked
screen.listen()
screen.onkey(fun=player.move_forward, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(player.game_speed)
    screen.update()

#TODO: Get cars to move
    for car in cars:
        car.move()
        if car.xcor() < -300:
            car.setx(300)

        if car.distance(player) <20:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() > 300:
        player.next_level()
        scoreboard.next_level()
        print(player.game_speed)

screen.exitonclick()