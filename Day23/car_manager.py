from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

class CarManager(Turtle):
  
  def __init__(self, speed):
    super().__init__()
    self.startingPos = (320, random.randint(-250, 270))
    self.exist = True
    self.moveSpeed = speed
    self.penup()
    self.color(random.choice(COLORS))
    self.shape("square")
    self.shapetransform(1.0, 0.0, -0.0, 2.0)
    self.goto(self.startingPos)
    self.setheading(180)
    if self.exist == False:
      return

  def carsGo(self):
    if self.xcor() > -320:
      self.forward(self.moveSpeed)
    else:
      self.clear()
      self.hideturtle()
      self.exist = False
