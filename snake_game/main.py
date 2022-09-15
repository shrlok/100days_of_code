from turtle import Screen, Turtle
import time
# Screen setting
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
starting_position = ((0, 0), (-20, 0), (-40, 0))

segments = []

# Snake's body description
def snake_body(pos):
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(pos)
    segments.append(new_segment)

# Creating snake's body
for position in starting_position:
    snake_body(position)


game_in_on = True
while game_in_on:
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(segments)-1, 0, -1):
        new_x = segments[seg_num-1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)

    segments[0].forward(20)
    if segments[0].xcor() >= 300:
        game_in_on = False
# Screen exit func
screen.exitonclick()