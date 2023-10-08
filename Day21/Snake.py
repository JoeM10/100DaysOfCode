from turtle import Turtle, Screen
MOVEDISTANCE = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
  def __init__(self):
    self.squares = []
    self.createSnake()
    self.head = self.squares[0]
  
  def createSnake(self):
    for position in STARTING_POSITIONS:
      self.addSegment(position)
  
  def addSegment(self, position):
    square = Turtle(shape="square")
    square.color("white")
    square.penup()
    square.goto(position)
    self.squares.append(square)

  def extend(self):
    self.addSegment(self.squares[-1].position())
  
  def moveSnake(self):
    for segment in range(len(self.squares) - 1, 0, -1):
      newX = self.squares[segment - 1].xcor()
      newY = self.squares[segment - 1].ycor()
      self.squares[segment].goto(newX, newY)
    self.head.forward(MOVEDISTANCE)

  def up(self):
    if self.head.heading() != DOWN:
      self.head.setheading(UP)

  def down(self):
    if self.head.heading() != UP:
      self.head.setheading(DOWN)

  def left(self):
    if self.head.heading() != RIGHT:
      self.head.setheading(LEFT)

  def right(self):
    if self.head.heading() != LEFT:
      self.head.setheading(RIGHT)
