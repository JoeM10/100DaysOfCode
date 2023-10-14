from turtle import Turtle

UP = 90
DOWN = 270
SPEED = 40


class Paddle(Turtle):
  
  def __init__(self, position):
    super().__init__()
    self.shape("square")
    self.penup()
    self.shapetransform(1.0, 0.0, -0.0, 5.0)
    self.left(90)
    self.goto(position)
    self.color("white")

  def up(self):
    if self.ycor() < 390:
      self.forward(SPEED)

  def down(self):
    if self.ycor() > -390:
      self.backward(SPEED)

