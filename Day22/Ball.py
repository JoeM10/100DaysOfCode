from turtle import Turtle

SPEED = 5
ON = True

class Ball(Turtle):

  def __init__(self):
    super().__init__()
    self.shape("circle")
    self.penup()
    self.color("white")
    self.goto(0, 0)
    self.left(45)

  def moveBall(self):
    if self.ycor() >= 442 or self.ycor() <= -442:
      self.bounce()
    self.forward(5)

  def bounce(self):
    self.right(90)