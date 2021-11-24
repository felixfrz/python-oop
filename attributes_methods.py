# OOP Attributes and Methods
# from turtle import Turtle, Screen

# timmy = Turtle()

# timmy.shape('turtle')
# timmy.color('green')
# timmy.forward(distance=100)

# my_screen = Screen()

# print(my_screen.canvheight)

# my_screen.exitonclick()


from prettytable import PrettyTable

table = PrettyTable()

table.add_column('States In Nigeria', ['Lagos', 'Ondo', 'Rivers', 'Cross Rivers'])
table.add_column('Capital', ['Ikeja', 'Akure', 'Port Harcourt', 'Calabar'])

# Attribute
table.align = 'l' #left aligment

print(table)