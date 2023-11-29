import turtle
import os
import pandas
from stateNamePrinter import StateNamePrinter

scriptDirectory = os.path.dirname(__file__)
statesData = pandas.read_csv(f"{scriptDirectory}\\50_states.csv")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = f"{scriptDirectory}\\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

printState = StateNamePrinter
winPrinter = StateNamePrinter("", (0, 0))
guessedStates = []
stateNames = statesData.state.to_list()
statesDict = dict(zip(statesData.state, zip(statesData.x, statesData.y)))
usedStatesList = []
gameOn = True
while gameOn:
  if guessedStates == 50:
    winPrinter.win()
    gameOn = False
  else:
    answerState = screen.textinput(title=f"{len(guessedStates)}/50 States Correct", prompt="What's another state's name?").title()
    stateCoordinate = ()

    if answerState == "Exit":
      [stateNames.remove(state) for state in usedStatesList]
      stateDataFrame = pandas.DataFrame(stateNames)
      stateDataFrame.to_csv(f"{scriptDirectory}\\StatesToLearn.csv")
      turtle.bye()

    elif answerState in statesDict and answerState not in usedStatesList:
      usedStatesList.append(answerState)
      stateCoordinate = statesDict[answerState]
      printState(state=answerState, position=stateCoordinate)
      guessedStates.append(answerState)

  # KEEP AT BOTTOM--------
turtle.mainloop()