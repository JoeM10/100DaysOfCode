from turtle import Screen
from Snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

gameOn = True
while gameOn:
  screen.update()
  time.sleep(0.1)
  snake.moveSnake()

  # Detect collision with food.
  if snake.head.distance(food) < 15:
    food.refresh()
    snake.extend()
    scoreboard.increaseScore()

  # Detect collison with wall.
  if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
    food.refresh()
    scoreboard.reset()
    snake.reset()

  # Detect collison with tail.
  for square in snake.squares[1:]: 
    if snake.head.distance(square) < 10:
      food.refresh()
      scoreboard.reset()
      snake.reset()

# KEEP AT BOTTOM--------
screen.exitonclick()