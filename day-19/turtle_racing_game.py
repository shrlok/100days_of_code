from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turlte will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
# tim = Turtle(shape="turtle")
# tim.penup()
# tim.goto(x=-230, y=-100)

start_x = -230
start_y = -100
def create_turtle(y_position, color):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x= -230 , y= y_position)
    new_turtle.color(color)
    all_turtles.append(new_turtle)


for color in colors:
    create_turtle(y_position= start_y, color=color)
    start_y += 40


if user_bet:
    is_race_on = True


while is_race_on:


    for turtle in all_turtles:
        if turtle.xcor() >= 150:
            wining_color = turtle.pencolor()
            if wining_color == user_bet:
                print(f"You've won! The {wining_color} turtle is the winner!")
            else:
                print(f"You've lost! The {wining_color} turtle is the winner!")
            is_race_on = False

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)




screen.exitonclick()
