from turtle import Turtle

FONT = ("Courier", 50, "normal")
ALIGNMENT = "center"

class GameOver(Turtle):
  
  def __init__(self):
    super().__init__()
    self.color("white")
    self.hideturtle()
    self.penup()
    self.goto(0, 0)

  def updateScoreboard(self):
    self.write("GAME  OVER", align=ALIGNMENT, font=FONT)