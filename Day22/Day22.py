from turtle import Turtle, Screen
from Paddle import Paddle
from Ball import Ball
from Scoreboard import Scoreboard
from GameOver import GameOver
import time


screen = Screen()

WIDTH = 1200
HEIGHT = 900

screen.setup(width=WIDTH, height=HEIGHT)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)
gameover = GameOver()
leftPaddle = Paddle((WIDTH / -2 + 40, 0))
rightPaddle = Paddle((WIDTH / 2 - 40, 0))
ball = Ball()
leftScore = Scoreboard((-70, 400))
rightScore = Scoreboard((70, 400))

# Middle line of screen.
middleLine = Turtle()
middleLine.hideturtle()
middleLine.speed(0)
middleLine.pencolor("white")
middleLine.pensize(15)
middleLine.penup()
middleLine.goto(0, HEIGHT / 2)
middleLine.right(90)
for _ in range(18):
  middleLine.pendown()
  middleLine.forward(25)
  middleLine.penup()
  middleLine.forward(30)

# Controls.
screen.listen()
screen.onkey(leftPaddle.up, "w")
screen.onkey(leftPaddle.down, "s")
screen.onkey(rightPaddle.up, "Up")
screen.onkey(rightPaddle.down, "Down")

gameOn = True
while gameOn:
  screen.update()
  ball.moveBall()
  time.sleep(0.01)

# Detect collision with paddle.
  if abs(ball.xcor() - leftPaddle.xcor()) <= 23 and abs(ball.ycor() - leftPaddle.ycor()) <= 55:
    ball.bounce()

  if abs(ball.xcor() - rightPaddle.xcor()) <= 23 and abs(ball.ycor() - rightPaddle.ycor()) <= 55:
    ball.bounce()
  
# Detect if ball hit goal.
  if ball.xcor() <= -600:
    rightScore.increaseScore()
    ball.goto(0,0)
    leftPaddle.goto(WIDTH / -2 + 40, 0)
    rightPaddle.goto(WIDTH / 2 - 40, 0)

  if ball.xcor() >= 600:
    leftScore.increaseScore()
    ball.goto(0,0)
    leftPaddle.goto(WIDTH / -2 + 40, 0)
    rightPaddle.goto(WIDTH / 2 - 40, 0)
  
# End Game.
  if leftScore.score == 5 or rightScore.score == 5:
    gameover.updateScoreboard()
    gameOn = False

# KEEP AT BOTTOM--------
screen.exitonclick()