import ColorData
import os
import turtle as T
import random
import colorgram
timmy = T
timmy.shape("turtle")
timmy.colormode(255)
timmy.speed(0)


# for _ in range(4):
#   timmy.forward(50)
#   timmy.left(90)

# for _ in range(15):
#   timmy.forward(10)
#   timmy.up()
#   timmy.forward(10)
#   timmy.down()

# Makes timmy a random color.----
# def randomColor():
#   red = random.randint(0, 255)
#   green = random.randint(0, 255)
#   blue = random.randint(0, 255)
#   timmy.color(red, green, blue)

# Will make shapes.----
# numSides = 20
# while numSides <= 25:
#   for _ in range(numSides):
#     angle = 360 / numSides
#     timmy.forward(10)
#     timmy.right(angle)
#   numSides += 1
#   randomColor()

# Will make random colored lines in random directions.----
# turn = [0, 90, 180, 270]
# timmy.speed(0)
# timmy.pensize(15)

# for _ in range(500):
#   timmy.forward(25)
#   timmy.right(random.choice(turn))
#   randomColor()

# Makes a spirograph----
# spin = 0
# while spin < 360:
#   timmy.circle(200)
#   randomColor()
#   timmy.right(8)
#   spin += 8

# Hirst Dots Painting Project------

timmy.pensize(15)

def drawRow():
  timmy.dot(20, random.choice(ColorData.rgb))
  timmy.forward(50)

def nextRow():
  timmy.right(180)
  timmy.forward(500)
  timmy.right(90)
  timmy.forward(50)
  timmy.right(90)

timmy.penup()
row = 0
while row < 10:
  for _ in range(10):
    drawRow()
  nextRow()
  row += 1


# KEEP AT BOTTOM---
screen = timmy.Screen()
screen.exitonclick()
