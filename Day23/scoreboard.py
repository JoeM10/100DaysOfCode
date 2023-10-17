from turtle import Turtle

FONT = ("Courier", 20, "normal")
ALIGNMENT = "left"
POSITION = (-280, 255)

class Scoreboard(Turtle):
  
  def __init__(self):
    super().__init__()
    self.penup()
    self.score = 1
    self.color("black")
    self.hideturtle()
    self.goto(POSITION)
    self.updateScoreboard()

  def updateScoreboard(self):
    self.write(f"Level: {self.score}", align=ALIGNMENT, font=FONT)

  def increaseScore(self):
    self.score += 1
    self.clear()
    self.updateScoreboard()
  
