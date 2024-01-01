from tkinter import *
import os
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
QUESTION_FONT = ("Arial", 20, "italic")
SCORE_FONT = ("Arial", 14, "normal")
scriptDirectory = os.path.dirname(__file__)

class QuizInterface:

  def __init__(self, quiz_brain: QuizBrain):

    self.quiz = quiz_brain

    self.window = Tk()
    self.window.title("Quizzler")
    self.window.config(bg=THEME_COLOR)

    # Question Canvas.
    self.questionCanvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
    self.questionCanvasText = self.questionCanvas.create_text(150, 125, width=280, text="Testing 1 2 3", fill="black", font=QUESTION_FONT)
    self.questionCanvas.grid(column=0, columnspan=2, row=1, pady=20, padx=20)

    # True Button.
    self.trueButtonImage = PhotoImage(file=f"{scriptDirectory}\\images\\true.png")
    self.trueButton = Button(image=self.trueButtonImage, highlightthickness=0, command=self.truePressed)
    self.trueButton.grid(column=0, row=2, padx=20, pady=20)

    # False Button.
    self.falseButtonImage = PhotoImage(file=f"{scriptDirectory}\\images\\false.png")
    self.falseButton = Button(image=self.falseButtonImage, highlightthickness=0, command=self.falsePressed)
    self.falseButton.grid(column=1, row=2, padx=20, pady=20)

    # Score Text.
    self.scoreText = Label(text=f"Score: 0", font=SCORE_FONT, bg=THEME_COLOR, fg="white", highlightthickness=0)
    self.scoreText.grid(column=1, row=0, padx=20, pady=20)

    self.getNextQuestion()

    # KEEP AT BOTTOM ----------
    self.window.mainloop()

  def getNextQuestion(self):
    self.questionCanvas.config(bg="white")
    if self.quiz.still_has_questions():
      questionText = self.quiz.next_question()
      self.scoreText.config(text=f"Score: {self.quiz.score}")
      self.questionCanvas.itemconfig(self.questionCanvasText, text=questionText)
    else:
      self.questionCanvas.itemconfig(self.questionCanvasText, text="You've reached the end of the quiz!")
      self.trueButton.config(state="disabled")
      self.falseButton.config(state="disabled")

  def truePressed(self):
    self.giveFeedback(self.quiz.check_answer("True"))
  
  def falsePressed(self):
    self.giveFeedback(self.quiz.check_answer("False"))

  def giveFeedback(self, isRight):
    if isRight == True:
      self.questionCanvas.config(bg="green")
    elif isRight == False:
      self.questionCanvas.config(bg="red")
    self.window.after(1000, func=self.getNextQuestion)
