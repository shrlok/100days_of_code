from turtle import Turtle, Screen, colormode
import random

tim = Turtle()
colormode(255)
corner = 15
tim.shape("turtle")
tim.speed(0)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)
def draw_spirograf(size_of_gap):
    for _ in range(int(350 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograf(5)

screen = Screen()
screen = Screen().exitonclick()