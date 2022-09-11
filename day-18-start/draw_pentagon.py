from turtle import Turtle, Screen
import random
tim = Turtle()
tim.shape("turtle")
# tim.color("blue", "yellow")
walk = 3

def pentagon(corner_nums):
    corner = 360 / corner_nums
    for _ in range(corner_nums):
        tim.color(random_color())
        tim.right(corner)
        tim.forward(100)

def random_color():
    return random.random()

for walk in range(3, 11):
    tim.color(random_color(), random_color(), random_color())
    pentagon(walk)

