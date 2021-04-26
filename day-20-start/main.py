from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Xenzio")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

# Move Snake
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    y = snake.head.ycor()
    x = snake.head.xcor()
    if x > 300 or x < -300 or y > 300 or y < -300:
        snake.reset()
        scoreboard.reset()

    #Detect collision with tail
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            snake.reset()
            scoreboard.reset()



screen.exitonclick()

