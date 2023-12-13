from tkinter import *
import os
import pandas
import random

# ---------------------------- CONSTANTS ---------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
scriptDirectory = os.path.dirname(__file__)

# ---------------------------- VARIABLES ---------------------------- #
try:
  wordsFromCSV = pandas.read_csv(f"{scriptDirectory}\\data\\wordsToLearn.csv")
except FileNotFoundError:
  wordsFromCSV = pandas.read_csv(f"{scriptDirectory}\\data\\french_words.csv")
wordsDict = wordsFromCSV.to_dict(orient="records")
wordsDictDataFrame = pandas.DataFrame(wordsDict)
currentWord = random.choice(wordsDict)

# ---------------------------- RIGHT NEW WORD ---------------------------- #
def rightNewCard():
  global currentWord, flipTimer, wordsDictDataFrame
  window.after_cancel(flipTimer)
  currentWord = random.choice(wordsDict)
  newLearningWord = currentWord[wordsFromCSV.columns[0]]
  flashcardCanvas.itemconfig(flashCardImageDisplay, image=frontFlashcardImage)
  flashcardCanvas.itemconfig(wordText, fill="black", text=newLearningWord.title())
  flashcardCanvas.itemconfig(languageText, fill="black", text=wordsFromCSV.columns[0])
  # Removing known words.
  wordsDict.remove(currentWord)
  # Adding them to a seperate .csv for learning.
  wordsDictDataFrame = pandas.DataFrame(wordsDict)
  wordsDictDataFrame.to_csv(f"{scriptDirectory}\\data\\wordsToLearn.csv", mode='w', index=False)
  
  flipTimer = window.after(3000, func=flipCard)

# ---------------------------- WRONG NEW WORD ---------------------------- #
def wrongNewCard():
  global currentWord, flipTimer
  window.after_cancel(flipTimer)
  currentWord = random.choice(wordsDict)
  newLearningWord = currentWord[wordsFromCSV.columns[0]]
  flashcardCanvas.itemconfig(flashCardImageDisplay, image=frontFlashcardImage)
  flashcardCanvas.itemconfig(wordText, fill="black", text=newLearningWord.title())
  flashcardCanvas.itemconfig(languageText, fill="black", text=wordsFromCSV.columns[0])
  flipTimer = window.after(3000, func=flipCard)

# ---------------------------- FLIP CARD ---------------------------- #
def flipCard():
  flashcardCanvas.itemconfig(flashCardImageDisplay, image=backFlashcardImage)
  flashcardCanvas.itemconfig(languageText, fill="white", text=wordsFromCSV.columns[1])
  flashcardCanvas.itemconfig(wordText, fill="white", text=currentWord[wordsFromCSV.columns[1]].title())

# ---------------------------- UI SETUP ---------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flipTimer = window.after(3000, func=flipCard)

# Flashcard canvas.
flashcardCanvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
frontFlashcardImage = PhotoImage(file=f"{scriptDirectory}\\images\\card_front.png")
backFlashcardImage = PhotoImage(file=f"{scriptDirectory}\\images\\card_back.png")
flashCardImageDisplay = flashcardCanvas.create_image(400, 268, image=frontFlashcardImage)
flashcardCanvas.grid(column=0, columnspan=2, row=0)

# Language text.
languageText = flashcardCanvas.create_text(400, 150, text=wordsFromCSV.columns[0], fill="black", font=LANGUAGE_FONT)

# Word text.
wordText = flashcardCanvas.create_text(400, 263, text="", fill="black", font=WORD_FONT)

# Right button.
rightButtonImage = PhotoImage(file=f"{scriptDirectory}\\images\\right.png")
rightButton = Button(image=rightButtonImage, highlightthickness=0, command=rightNewCard)
rightButton.grid(column=1, row=1)

# Wrong button.
wrongButtonImage = PhotoImage(file=f"{scriptDirectory}\\images\\wrong.png")
wrongButton = Button(image=wrongButtonImage, highlightthickness=0, command=wrongNewCard)
wrongButton.grid(column=0, row=1)

# KEEP AT BOTTOM--------
wrongNewCard()
window.mainloop()