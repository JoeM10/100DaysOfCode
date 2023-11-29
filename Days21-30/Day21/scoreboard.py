from turtle import Turtle
import os

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):

  def __init__(self):
    super().__init__()
    self.scriptDirectory = os.path.dirname(__file__)
    with open(f"{self.scriptDirectory}\\data.txt") as file:
      self.highScoreData = int(file.read().strip())
    self.score = 0
    self.highScore = self.highScoreData
    self.color("white")
    self.hideturtle()
    self.penup()
    self.goto(0, 270)
    self.updateScoreboard()

  def updateScoreboard(self):
    self.clear()
    self.write(f"Score: {self.score} | High-Score: {self.highScore}", align=ALIGNMENT, font=FONT)

  def increaseScore(self):
    self.score += 1
    self.updateScoreboard()
  
  def reset(self):
    if self.score > self.highScore:
      self.highScore = self.score
    with open(f"{self.scriptDirectory}\\data.txt", mode="w") as file:
      file.write(f"{self.highScore}")
    self.score = 0
    self.updateScoreboard()