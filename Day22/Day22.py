# NOTES--------
# 1.) Setup Screen✅
# 2.) Middle line✅
# 3.) Player✅ and CPU
# 4.) Ball
# 5.) Score

from turtle import Turtle, Screen
from Paddle import Paddle
from Ball import Ball
import time


screen = Screen()

WIDTH = 1200
HEIGHT = 900

screen.setup(width=WIDTH, height=HEIGHT)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)
leftPaddle = Paddle((WIDTH / -2 + 40, 0))
rightPaddle = Paddle((WIDTH / 2 - 40, 0))
ball = Ball()


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

screen.listen()
screen.onkey(leftPaddle.up, "w")
screen.onkey(leftPaddle.down, "s")
screen.onkey(rightPaddle.up, "Up")
screen.onkey(rightPaddle.down, "Down")

gameOn = True
while gameOn:
  screen.update()
  ball.moveBall()
  time.sleep(0.08)

  # Detect collision with paddle.
  ball.position()

  if ball.distance(leftPaddle.xcor() + 10, leftPaddle.ycor()) < 35 or ball.distance(rightPaddle.xcor() - 35, rightPaddle.ycor()) < 40:
    ball.bounce()
# KEEP AT BOTTOM--------
screen.exitonclick()