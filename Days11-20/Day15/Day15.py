from CoffeeData import MENU
from CoffeeData import resources

def drinkSelection():
  while True:
    drink = str(input("  What would you like? (espresso/latte/cappuccino): ")).lower()
    print(f"You have selected: {drink}.")
    if drink in ["espresso", "latte", "cappuccino", "report", "off"]:
      return drink
    else:
      print("Invalid input, please enter 'espresso', 'latte', or 'cappuccino'.")

def report():
  print(f"Water: {resources['water']}ml")
  print(f"Milk: {resources['milk']}ml")
  print(f"Coffee: {resources['coffee']}g")
  print(f"Money: ${resources['money']:.2f}")

def functions():
  userInput = drinkSelection()
  if userInput == "off":
    print("Turning off.")
    exit()
  elif userInput == "report":
    report()
    return
  
  elif userInput in MENU:
    drink = MENU[userInput]
    ingredients = drink["ingredients"]
    try:
      for ingredient, quantity in ingredients.items():
          if resources[ingredient] >= quantity:
            continue
          else:
            raise Exception(f"Insufficient {ingredient}. Please add more then try again.")
          
    except Exception as e:
      print(f"Error: {e}")
      print("Turning off.")
      exit()

  if moneyStuff(userInput) == 0:
    return
  else:
    for ingredient, quantity in ingredients.items():
      if resources[ingredient] >= quantity:
        resources[ingredient] -= quantity
  print(f"Here is your {userInput} ☕. Enjoy!")

def moneyStuff(userInput):
  drink = MENU[userInput]
  print(f'Please insert ${drink["cost"]:.2f}')
  while True:
    while True:
      try:
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))
        break
      except ValueError:
        print("Invalid input. Please enter numbers only.")
  
    moneyInserted = round((quarters*0.25) + (dimes*0.10) + (nickles*0.05) + (pennies*0.01), 2)
    if moneyInserted >= drink["cost"]:
      break
    else:
      print("Sorry, that's not enough money. Money refunded.")
      return 0
      
  print(f"Amount inserted: ${moneyInserted:.2f}")
  change = round(moneyInserted - drink["cost"], 2)
  print(f"Here is ${change} in change.")
  afterRefund = moneyInserted - change
  resources["money"] += afterRefund
  return afterRefund

while True:
  functions()
