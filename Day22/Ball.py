from turtle import Turtle
import random

SPEED = 5
ON = True
STARTING_DIRECTIONS = [45, 135, 225, 315]
RANDOM_DIRECTION = random.choice(STARTING_DIRECTIONS)

class Ball(Turtle):

  def __init__(self):
    super().__init__()
    self.shape("circle")
    self.penup()
    self.color("white")
    self.goto(0, 0)
    self.left(RANDOM_DIRECTION)

  def moveBall(self):
    if self.ycor() >= 442 or self.ycor() <= -442:
      self.bounce()
    self.forward(5)

  def bounce(self):
    if RANDOM_DIRECTION == 45 or RANDOM_DIRECTION == 225:
      self.right(90)
    else:
      self.left(90)