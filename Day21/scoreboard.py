from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):

  def __init__(self):
    super().__init__()
    self.score = 0
    self.color("white")
    self.hideturtle()
    self.penup()
    self.goto(0, 270)
    self.updateScoreboard()

  def updateScoreboard(self):
    self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

  def increaseScore(self):
    self.score += 1
    self.clear()
    self.updateScoreboard()
  
  def gameOver(self):
    self.goto(0, 0)
    self.write("GAME OVER", align=ALIGNMENT, font=FONT)
