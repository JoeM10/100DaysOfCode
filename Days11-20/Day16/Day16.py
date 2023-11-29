# from turtle import Turtle, Screen

# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("red")

# timmy.forward(100)

# myScreen = Screen()
# print(myScreen.canvheight)
# myScreen.exitonclick()

# from prettytable import PrettyTable

# table = PrettyTable()

# table.add_column("Pokemon", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])
# table.align = "l"

# print(table)

# OOP Coffee Machine Project-------
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

is_on = True

while is_on:
  options = menu.get_items()
  choice = input(f"What would you like? ({options}): ").lower()
  if choice == "off":
    is_on = False
  elif choice == "report":
    coffee_maker.report()
    money_machine.report()
  else:
    drink = menu.find_drink(choice)
    if coffee_maker.is_resource_sufficient(drink):
      if money_machine.make_payment(drink.cost):
        coffee_maker.make_coffee(drink)
