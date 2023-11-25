from tkinter import *
import os
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
scriptDirectory = os.path.dirname(__file__)
# ---------------------------- TIMER RESET ------------------------------- # 
def resetTimer():
  global reps
  window.after_cancel(timer)
  canvas.itemconfig(timerCountDown, text="00:00")
  reps = 0
  checkmarks.config(text="")
  timerText.config(text="Timer", fg=GREEN)

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def startTimer():
  global reps
  global timerText
  reps += 1
  workSeconds = WORK_MIN * 60
  shortBreakSeconds = SHORT_BREAK_MIN * 60
  longBreakSeconds = LONG_BREAK_MIN * 60
  # If it's the 1st/3rd/5th/7th rep:
  if reps % 2 == 1:
    countDown(workSeconds)
    timerText.config(text="Work", fg=GREEN)
  # If it's the 8th rep:
  elif reps % 8 == 0:
    countDown(longBreakSeconds)
    timerText.config(text="Break", fg=RED)
  # If it's the 2nd/4th/6th rep:
  elif reps % 2 == 0:
    countDown(shortBreakSeconds)
    timerText.config(text="Break", fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countDown(count):
  global reps
  global timer
  checkamount = ""
  countMinute = math.floor(count / 60)
  if countMinute < 10:
    countMinute = f"0{countMinute}"

  countSecond = count % 60
  if countSecond < 10:
    countSecond = f"0{countSecond}"

  canvas.itemconfig(timerCountDown, text=f"{countMinute}:{countSecond}")
  if count > 0:
    timer = window.after(1000, countDown, count-1)
  else:
    startTimer()
    for _ in range(1,reps,2):
      checkamount += "✔"
      checkmarks.config(text=f"{checkamount}")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Image of tomato.
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomatoImage = PhotoImage(file=f"{scriptDirectory}\\tomato.png")
canvas.create_image(100, 112, image=tomatoImage)

# Timer countdown text.
timerCountDown = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Text that says "Timer"
timerText = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW, highlightthickness=0)
timerText.grid(column=1, row=0)

# Start button.
startButton = Button(text="Start", highlightthickness=0, command=startTimer)
startButton.grid(column=0, row=2)

# Reset button.
resetButton = Button(text="Reset", highlightthickness=0, command=resetTimer)
resetButton.grid(column=2, row=2)

# Checkmark text ✔.
checkmarks = Label(fg=GREEN, bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 15, "normal"))
checkmarks.grid(column=1, row=3) 

# KEEP AT BOTTOM--------
window.mainloop()