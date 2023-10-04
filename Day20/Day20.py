from turtle import Turtle, Screen
from Snake import Snake
import time
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


gameOn = True
while gameOn:
  screen.update()
  time.sleep(0.2)

  snake.moveSnake()

# KEEP AT BOTTOM--------
screen.exitonclick()