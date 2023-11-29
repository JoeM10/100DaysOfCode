from turtle import Turtle, Screen
import random
import os

screen = Screen()
# timmy = Turtle()

# def moveForwards():
#   timmy.forward(10)

# def moveBackwards():
#   timmy.backward(10)

# def turnLeft():
#   timmy.left(5)

# def turnRight():
#   timmy.right(5)

# def clear():
#   timmy.clear()
#   timmy.penup()
#   timmy.home()
#   timmy.pendown()

# screen.listen()

# screen.onkey(key="w", fun=moveForwards)
# screen.onkey(key="s", fun=moveBackwards)
# screen.onkey(key="a", fun=turnLeft)
# screen.onkey(key="d", fun=turnRight)
# screen.onkey(key="c", fun=clear)

# Turtle Race Game--------

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

screen.setup(width=500, height=400)
userBet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color: ")
turtles = []

isRaceOn = False

num = 0
yAxis = -75
for turtle in range(6):
  newTurt = Turtle(shape="turtle")
  newTurt.color(colors[num])
  newTurt.penup()
  newTurt.goto(x=-230, y=yAxis)
  turtles.append(newTurt)
  num += 1
  yAxis += 30

if userBet:
  isRaceOn = True

while isRaceOn:
  
  for turtle in turtles:
    if turtle.xcor() > 230:
      winningColor = turtle.pencolor()
      if winningColor == userBet:
        print(f"You've won! The {winningColor} turtle is the winner!")
        isRaceOn = False
      else:
        print(f"You lost! The {winningColor} turtle is the winner!")
        isRaceOn = False

    randDistance = random.randint(0, 10)
    turtle.forward(randDistance)

# KEEP AT BOTTOM--------
screen.exitonclick()