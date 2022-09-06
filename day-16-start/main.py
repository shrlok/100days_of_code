# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("#285078", "#a0c8f0")
# timmy.forward(100)
# my_screen = Screen()
#
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon name", ["Picachu", "Squirtle", "Charmander"])
table.add_column(("Type"), ["Electric", "Watrer", "Fire"])
table.align = "l"

print(table)
