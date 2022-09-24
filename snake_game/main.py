from turtle import Screen, Turtle
from snake import Snake
import time
# Screen setting
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()


game_in_on = True
while game_in_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.segments[0].xcor() >= 300:
        game_in_on = False
# Screen exit func
screen.exitonclick()