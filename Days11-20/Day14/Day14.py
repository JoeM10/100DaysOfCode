
import random
import art
import game_data
import os

def accountInfo(account):
  name, description, country = account["name"], account["description"], account["country"]
  return f"{name}, a {description}, from {country}."

def score(currentScore):
  if currentScore > 0:
    print(f"You're right! Current score: {currentScore}.")

def followerCompare(accountA, accountB, currentScore):
  followersA = accountA["follower_count"]
  followersB = accountB["follower_count"]
  correctAnswer = "a" if followersA > followersB else "b"
  
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
  accountA = random.choice(game_data.data)
  while True:
    accountB = random.choice(game_data.data)
    if accountA == accountB:
      accountB = random.choice(game_data.data)

    os.system('cls')
    print(art.logo)
    score(currentScore)

    print(f"Compare A: {accountInfo(accountA)}")
    print(art.vs)
    print(f"Compare B: {accountInfo(accountB)}")

    currentScore = followerCompare(accountA, accountB, currentScore)
    accountA = accountB

game()