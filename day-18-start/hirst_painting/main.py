# import colorgram
# colors = colorgram.extract("image.jpg", 30)
# color_list = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_list.append((r, g, b))
#
# print(color_list)
import turtle
import random
color_list  = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

def random_color():
    color = random.choice(color_list)
    return  color

tim = turtle.Turtle()
turtle.colormode(255)
position_x = -300
position_y = -300
tim.penup()
tim.hideturtle()


for _ in range(10):

    tim.setposition(position_x, position_y)
    position_y += 50
    for _ in range(10):
        tim.dot(20, random_color())
        tim.forward(50)

screen = turtle.Screen()
screen.exitonclick()