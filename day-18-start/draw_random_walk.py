import turtle
from turtle import Turtle, Screen
import random
corner = [0, 90, 180, 270]

tim = Turtle()
turtle.colormode(255)

tim.shape("turtle")
tim.speed(0)
tim.pensize(10)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

for _ in range(100):
    tim.color(random_color())
    tim.setheading(random.choice(corner))
    tim.forward(30)


