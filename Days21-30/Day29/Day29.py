from tkinter import *
from tkinter import messagebox
import os
import random
import pyperclip
# ---------------------------- CONSTANTS ------------------------------- #
FONT = ("Futura", 10, "bold")
scriptDirectory = os.path.dirname(__file__)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generatePassword():
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  nr_letters = random.randint(8, 10)
  nr_symbols = random.randint(2, 4)
  nr_numbers = random.randint(2, 4)

  password_list = []

  [password_list.append(random.choice(letters)) for char in range(nr_letters)]
  password_list += [random.choice(symbols) for char in range(nr_symbols)]
  password_list += [random.choice(numbers) for char in range(nr_numbers)]

  random.shuffle(password_list)

  randomPassword = "".join(password_list)

  passwordInput.delete(0, END)
  passwordInput.insert(0, randomPassword)
  pyperclip.copy(randomPassword)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
  website = websiteInput.get()
  emailUsername = emailUsernameInput.get()
  password = passwordInput.get()
  if len(website) == 0 or len(emailUsername) == 0 or len(password) == 0:
    messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
  else:
    isOk = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail/Username: {emailUsername}\nPassword: {password}\nIs it ok to save?")

    if isOk:
      with open(f"{scriptDirectory}\\data.txt", mode='a') as dataFile:
        dataFile.write(f"{website} | {emailUsername} | {password}\n")
      websiteInput.delete(0, END)
      passwordInput.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="white")

# Image of lock.
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
lockImage = PhotoImage(file=f"{scriptDirectory}\\logo.png")
canvas.create_image(100, 100, image=lockImage)
canvas.grid(column=0, columnspan=3, row=0)

# Website text.
websiteText = Label(text="Website:", font=FONT, bg="white", highlightthickness=0)
websiteText.grid(column=0, row=1)

# Website Input.
websiteInput = Entry(width=48)
websiteInput.grid(column=1, columnspan=2, row=1)
websiteInput.focus()

# Email/Username text.
emailUsernameText = Label(text="Email/Username:", font=FONT, bg="white", highlightthickness=0)
emailUsernameText.grid(column=0, row=2)

# Email/Username Input.
emailUsernameInput = Entry(width=48)
emailUsernameInput.grid(column=1, columnspan=2, row=2)
emailUsernameInput.insert(0, "example@email.com")

# Password text.
passwordText = Label(text="Password:", font=FONT, bg="white", highlightthickness=0)
passwordText.grid(column=0, row=3)

# Password Input.
passwordInput = Entry(width=25)
passwordInput.grid(column=1, row=3)

# Generate Password button.
generatePasswordButton = Button(text="Generate Password", font=FONT, highlightthickness=0, width=16, command=generatePassword)
generatePasswordButton.grid(column=2, row=3)

# Add button.
addButton = Button(text="Add", font=FONT, highlightthickness=0, width=32, command=save)
addButton.grid(column=1, columnspan=2, row=4)

# KEEP AT BOTTOM--------
window.mainloop()