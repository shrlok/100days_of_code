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
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_in_on = True
while game_in_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.segments[0].xcor() > 300:
        snake.segments[0].goto(-300,snake.segments[0].ycor())
    if snake.segments[0].xcor() < -300:
        snake.segments[0].goto(300, snake.segments[0].ycor())
    if snake.segments[0].ycor() > 300:
        snake.segments[0].goto(snake.segments[0].xcor(), -300)
    if snake.segments[0].xcor() < -300:
        snake.segments[0].goto(segments[0].xcor(), 300)
# Screen exit func
screen.exitonclick()