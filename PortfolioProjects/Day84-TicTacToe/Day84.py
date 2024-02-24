import random
import time

choices = {
  "row1" : [" ", " ", " "],
  "row2" : [" ", " ", " "],
  "row3" : [" ", " ", " "],
}

# Whoa
def winCondition() -> bool:
  first = choices["row1"]
  second = choices["row2"]
  third = choices["row3"]

  if first == ["X", "X", "X"] or second == ["X", "X", "X"] or third == ["X", "X", "X"]:
    print("You win!")
    return True
  
  elif first == ["O", "O", "O"] or second == ["O", "O", "O"] or third == ["O", "O", "O"]:
    print("You lose!")
    return True
  
  elif first[0] == "X" and second[0] == "X" and third[0] == "X":
    print("You Win!")
    return True
  
  elif first[1] == "X" and second[1] == "X" and third[1] == "X":
    print("You Win!")
    return True
  
  elif first[2] == "X" and second[2] == "X" and third[2] == "X":
    print("You Win!")
    return True
  
  elif first[0] == "X" and second[1] == "X" and third[2] == "X":
    print("You Win!")
    return True

  elif first[2] == "X" and second[1] == "X" and third[0] == "X":
    print("You Win!")
    return True

  elif first[0] == "O" and second[0] == "O" and third[0] == "O":
    print("You Lose!")
    return True
  
  elif first[1] == "O" and second[1] == "O" and third[1] == "O":
    print("You Lose!")
    return True
  
  elif first[2] == "O" and second[2] == "O" and third[2] == "O":
    print("You Lose!")
    return True
  
  elif first[0] == "O" and second[1] == "O" and third[2] == "O":
    print("You Lose!")
    return True

  elif first[2] == "O" and second[1] == "O" and third[0] == "O":
    print("You Lose!")
    return True
  
  elif " " not in first and " " not in second and " " not in third:
    print("It was a Stalemate!")
    return True

  else:
    return False


def welcome():
  askToPlay = input("Would you like to play Tic-Tac-Toe? 'Y' or 'N' : ").upper()
  while True:
    if askToPlay == "Y":
      print("Welcome to Tic-Tac-Toe!\n")
      return False
  
    elif askToPlay == "N":
      print("Goodbye!")
      exit()

    else:
      askToPlay = input("Please type 'Y' or 'N' : ").upper()


# Constructors for the board
def row1():
  row = f" {choices['row1'][0]} | {choices['row1'][1]} | {choices['row1'][2]} "
  return row
def row2():
  row = f" {choices['row2'][0]} | {choices['row2'][1]} | {choices['row2'][2]} "
  return row
def row3():
  row = f" {choices['row3'][0]} | {choices['row3'][1]} | {choices['row3'][2]} "
  return row
def board() -> bool:
  lines = "-----------"

  print(f"\n{row1()}")
  print(lines)
  print(row2())
  print(lines)
  print(f"{row3()}\n")

  return winCondition()


# Turn handling
def playerTurn():
  print("Please type the 'row#' and 'column#' where you want to play your piece.")
  print("EXAMPLE: row1 column2")

  playerInput = input("\nWhere would like to play your piece? : ").lower().split(" ")
  choosing = True
  row = ""
  column = ""

  while choosing:
    if playerInput[0] in ["row1", "row2", "row3"] and playerInput[1] in ["column1", "column2", "column3"]:
      row = playerInput[0]
      column = int(playerInput[1][-1]) -1

      if choices[row][column] == " ":
        choices[row][column] = "X"
        choosing = False

      else:
        playerInput = input("\nThat spot is already taken, please pick a different spot. : ").lower().split(" ")

    else:
      playerInput = input("\nPlease type the 'row#' and 'column#' where you want to play your piece. : ").lower().split(" ")


def cpuTurn():
  time.sleep(1.5)
  print("It is now the Cpu's turn.")
  time.sleep(2.5)

  choosing = True
  while choosing:
    row = f"row{random.randint(1,3)}"
    column = random.randint(0,2)
    if choices[row][column] == " ":
      choices[row][column] = "O"
      choosing = False

if __name__ == "__main__":
  while True:
    welcome()

    while board() == False:
      playerTurn()

      if winCondition() == False:
        board()
        cpuTurn()
