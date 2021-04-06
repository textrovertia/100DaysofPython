from turtle import Turtle, Screen

from prettytable import PrettyTable

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("blue")
timmy.forward(100)
timmy.right(90)
timmy.forward(100)
timmy.right(90)
timmy.forward(100)
timmy.right(90)
timmy.forward(100)


my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()


# Pretty table
table = PrettyTable()
table.add_column("Bible Books", ["Genesis", "Psalms", "Acts", "Proverbs"])
table.add_column("Authors", ["Moses", "David", "Luke", "Solomon"])

table.align = "l"
print(table)
