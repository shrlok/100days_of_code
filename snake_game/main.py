from turtle import Screen, Turtle
# Screen setting
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

# The len of the snake's bodies
body_len = range(3)
# Start position
start_x = 0
# Snake's body description
def snake_body(x_pos):
    snakes_square = Turtle(shape="square")
    snakes_square.color("white")
    snakes_square.penup()
    snakes_square.setposition(x= x_pos, y=0)

# Creating snake's body
for x in body_len:
    snake_body(start_x)
    start_x -=20

# Screen exit func
screen.exitonclick()