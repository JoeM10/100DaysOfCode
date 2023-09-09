
import random
import art
import game_data
import os

def compareA():
  comparisonA = random.choice(game_data.data)

  name = comparisonA['name']
  followerCount = comparisonA['follower_count']
  description = comparisonA['description']
  country = comparisonA['country']

  print(f"Compare A: {name}, {description}, from {country}.")
  return followerCount

def compareB():
  comparisonB = random.choice(game_data.data)

  name = comparisonB['name']
  followerCount = comparisonB['follower_count']
  description = comparisonB['description']
  country = comparisonB['country']

  print(f"Against B: {name}, {description}, from {country}.")
  return followerCount

def score(currentScore):
  if currentScore > 0:
    print(f"You're right! Current score: {currentScore}.")

def followerCompare(compareA, compareB, currentScore):
  correctAnswer = "a" if compareA > compareB else "b"
  
  playerGuess = str(input("Who has more followers? Type 'A' or 'B': ")).lower()
  if playerGuess == correctAnswer:
    currentScore += 1
    return currentScore
  else:
    os.system('cls')
    print(art.logo)
    print(f"Sorry, that's wrong. Final score: {currentScore}")
    exit()

def game():
  currentScore = 0
  while True:
    os.system('cls')
    print(art.logo)
    score(currentScore)

    compA = compareA()
    print(art.vs)
    compB = compareB()

    currentScore = followerCompare(compA, compB, currentScore)

game()
