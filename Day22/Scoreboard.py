from turtle import Turtle

FONT = ("Courier", 30, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):
  
  def __init__(self, position):
    super().__init__()
    self.score = 0
    self.color("white")
    self.hideturtle()
    self.penup()
    self.goto(position)
    self.updateScoreboard()

  def updateScoreboard(self):
    self.write(f"{self.score}", align=ALIGNMENT, font=FONT)

  def increaseScore(self):
    self.score += 1
    self.clear()
    self.updateScoreboard()