'''
# Roller Coaster Ticket Machine Project

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))

    if age >= 45 and age <= 55:
        print("Your ticket is free!.")
    elif age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")
        
    wantsPhoto = input("Do you want a photo taken? Y or N. ")
    if wantsPhoto == "Y" or wantsPhoto == "y":
        bill += 3
        
    print(f"Your total is ${bill}.")

else:
    print("Sorry, you have to grow taller before you can ride.")

# Comparison Operators
# ==  Equal
# !=  Not Equal
# >   Greater Than
# <   Less Than
# >=  Greater Than or Equal to
# <=  Less Than or Equal to

# Odd or Even Code Challenge

# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

# BMI 2.0 Calculator Project

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = round(weight / (height ** 2))

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")

elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")

elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")

elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")

else:
    print(f"Your BMI is {bmi}, you are clinically obese.")

#
# Is it a leap year? Program
#
# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")

#
# Pizza ordering program
#
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
cost = 0

if size == "S" or size == "s":
    cost = 15
    if add_pepperoni == "Y" or add_pepperoni == "y":
        cost += 2
        if extra_cheese == "Y" or extra_cheese == "y":
            cost += 1
            print(f"Your final bill is: ${cost}.")
        else:
            print(f"Your final bill is: ${cost}.")
    else:
        if extra_cheese == "Y" or extra_cheese == "y":
            cost += 1
            print(f"Your final bill is: ${cost}.")
        else:
            print(f"Your final bill is: ${cost}.")

elif size == "M" or size == "m":
    cost = 20
    if add_pepperoni == "Y" or add_pepperoni == "y":
        cost += 3
        if extra_cheese == "Y" or extra_cheese == "y":
            cost += 1
            print(f"Your final bill is: ${cost}.")
        else:
            print(f"Your final bill is: ${cost}.")

    else:
        if extra_cheese == "Y" or extra_cheese == "y":
            cost += 1
            print(f"Your final bill is: ${cost}.")
        else:
            print(f"Your final bill is: ${cost}.")


elif size == "L" or size == "l":
    cost = 25
    if add_pepperoni == "Y" or add_pepperoni == "y":
        cost += 3
        if extra_cheese == "Y" or extra_cheese == "y":
            cost += 1
            print(f"Your final bill is: ${cost}.")
        else:
            print(f"Your final bill is: ${cost}.")

    else:
        if extra_cheese == "Y" or extra_cheese == "y":
            cost += 1
            print(f"Your final bill is: ${cost}.")
        else:
            print(f"Your final bill is: ${cost}.")


else:
    print("Please try again.")

#
# Logical Operators
#
A and B
C or D
not E

#
# Love Calculator Program
#
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
lowerCaseName1 = name1.lower()
lowerCaseName2 = name2.lower()

numOfT = int(lowerCaseName1.count("t") + lowerCaseName2.count("t"))
numOfR = int(lowerCaseName1.count("r") + lowerCaseName2.count("r"))
numOfU = int(lowerCaseName1.count("u") + lowerCaseName2.count("u"))
numOfE = int(lowerCaseName1.count("e") + lowerCaseName2.count("e"))
totalOfTrue = str(numOfT + numOfR + numOfU + numOfE)

numOfL = int(lowerCaseName1.count("l") + lowerCaseName2.count("l"))
numOfO = int(lowerCaseName1.count("o") + lowerCaseName2.count("o"))
numOfV = int(lowerCaseName1.count("v") + lowerCaseName2.count("v"))
numOfE1 = int(lowerCaseName1.count("e") + lowerCaseName2.count("e"))
totalOfLove = str(numOfL + numOfO + numOfV + numOfE1)

trueLove = int(totalOfTrue + totalOfLove)

if trueLove <= 10 or trueLove >= 90:
    print(f"Your score is {trueLove}, you go together like coke and mentos.")

elif trueLove >= 40 and trueLove <= 50:
    print(f"Your score is {trueLove}, you are alright together.")
else:
    print(f"Your score is {trueLove}.")

'''

# Multi-block string - Using three ' will allow you to print multiple lines.

# Using a \ before seomthing will cause python to ignore it in a string. 
# - ex: "You\'re at a crossroads. Do you want to go 'Left' or 'Right', which do you choose?"

# Using \n at the end of a string will make another line.
# Useful for putting a input on a seperate line.
# -ex: str(input("Hello, how are you?\n"))

#
# Treasure Island Game Project
#


print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

action1 = str(input("What direction would you like to take first, 'Right' or 'Left'?\n")).lower()

def firstStep():
    if action1 == "left":
        print("You follow a path until you get to a shoreline.")

    elif action1 == "right":
        print("You take your first step and fall directly into a hole. GAME OVER!")
        quit()

    else:
        print("That was not a valid command.")
        quit()

firstStep()

print("You can see a island across the water. Do you wait for a boat, or swim across?")
action2 = str(input("Type 'Swim' or 'Wait'.\n")).lower()

def secondStep():
    if action2 == "wait":
        print("A boat eventually shows up and takes you across.")
    
    elif action2 == "swim":
        print("You were attacked by a sea serpent! GAME OVER!")
        quit()

    else:
        print("That was not a valid command.")
        quit()

secondStep()

print("On the island you find a Tomb. There is 3 doors inside the Tomb.")
action3 = str(input("Which door do you pick? 'Red', 'Blue', or 'Yellow'?\n")).lower()

def thirdStep():
    if action3 == "yellow":
        print("Congratulations you found the treasure! You win!")
        quit()
    
    elif action3 == "red":
        print("A huge swath of flame comes out of the door and singes you to a crisp. GAME OVER!")
        quit()
    
    elif action3 == "blue":
        print("A giant hand grabs you and pulls you into the dark. GAME OVER!")
        quit()
    
    else:
        print("That was not a valid command.")
        quit()

thirdStep()