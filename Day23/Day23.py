import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from GameOver import GameOver

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
gameOver = GameOver()
cars = []
carSpeed = 5


screen.listen()
screen.onkey(player.moveUp, "w")

game_is_on = True
while game_is_on:
  time.sleep(0.1)
  screen.update()
  carSpawnRate = random.randint(1, 4)
  if carSpawnRate == 1:
    newCar = CarManager(carSpeed)
    cars.append(newCar)
  for car in cars:
    car.carsGo()
    # If player hits car.
    if abs(car.xcor() - player.xcor()) <= 24 and abs(car.ycor() - player.ycor()) <= 20:
      gameOver.endGame()
      game_is_on = False
  # If player makes it to end.
  if player.ycor() == 280:
    carSpeed += 5
    scoreboard.increaseScore()
    player.reset()

# KEEP AT BOTTOM--------
screen.exitonclick()
