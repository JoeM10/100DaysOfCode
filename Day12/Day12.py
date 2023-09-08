import random
import art
import os

# Number Guessing Game Project.
# The program will generate a random number and the goal of the player is to guess the number.
# After each guess the program will tell you if you are too high or too low.
# There will be 2 difficulty modes, Easy and Hard.
# Easy will have 10 guesses while Hard will have 5.

def difficulty():
    while True:
      setting = str(input("Choose a difficulty. Type 'easy' or 'hard': "))
      if setting == "easy":
        return 10
      elif setting == "hard":
        return 5
      else:
        print("Invalid input, please type 'easy' or 'hard'.")

def randomNumber():
  randNum = random.randint(1, 101)
  # print(f"Testing: {randNum}")
  return randNum

def playerGuess():
  while True:
    try:
      guess = int(input("Make a guess: "))
      break
    except ValueError:
      print("Invalid Input, please type a number.")
  return guess

def game():
  os.system('cls')
  print(art.logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  guesses = difficulty()
  print(f"You have {guesses} attempts to guess the number.")
  randNum = randomNumber()
  guess = playerGuess()
  
  while not guesses == 1:
    if randNum == guess:
      print("You did it!")
      exit()
    elif randNum > guess:
      print("Too low.")
      print("Guess again.")
      guesses -= 1
      print(f"You have {guesses} guesses left.")
      guess = playerGuess()
    elif randNum < guess:
      print("Too high.")
      print("Guess again.")
      guesses -= 1
      print(f"You have {guesses} guesses left.")
      guess = playerGuess()
  print("You ran out of guesses. You lose!")

game() 