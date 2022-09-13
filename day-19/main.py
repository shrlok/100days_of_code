from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_back():
    tim.backward(10)

def counter_clockwise():
    tim.left(10)

def clockwise():
    tim.right(10)

def clear_drewing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="d", fun=counter_clockwise)
screen.onkey(key="a", fun=clockwise)
screen.onkey(key="c", fun=clear_drewing)
screen.exitonclick()