from turtle import Turtle

FONT = ("Courier", 8, "normal")
WINFONT = ("Courier", 100, "normal")
ALIGNMENT = "center"

class StateNamePrinter(Turtle):
  
  def __init__(self, state, position):
    super().__init__()
    self.penup()
    self.stateName = state
    self.color("black")
    self.hideturtle()
    self.goto(position)
    self.write(self.stateName, align=ALIGNMENT, font=FONT)

  def win(self):
    self.goto(0, -25)
    self.write("You Win!", align=ALIGNMENT, font=WINFONT)