from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont
import os

# ---------- CONSTANTS/GLOBALS ---------- #
FONT_NAME = "Roboto"
SCRIPT_DIRECTORY = os.path.dirname(__file__)
image = None
fontColor = None
# ---------- OPEN IMAGE ---------- #
def open_image():
  global image

  # Open file dialog to select an image file
  file_path = filedialog.askopenfilename()

  # Check if a file was selected
  if file_path:
    # Open the image file using PIL
    image = Image.open(file_path)

# ---------- WATER MARK IMAGE ---------- #
def watermark():
  global image
  global initialSelection

  if image != None:
    text = watermarkTextField.get()
    draw = ImageDraw.Draw(image)

    draw.text((75, image.size[1]-200), text, fill=initialSelection.get(), font=ImageFont.truetype("arial.ttf", 100))
    image.save(f"{SCRIPT_DIRECTORY}\\watermarkedImage.jpg")
  

# ---------- UI SETUP ---------- #
window = Tk()
window.title("Water Marker")
window.config(padx=35, pady=35, bg="white")

# Upload Image Button.
uploadImageButton = Button(text="Upload Image", font=(FONT_NAME, 12, "bold"), highlightthickness=0, \
command=open_image)
uploadImageButton.grid(column=0, row=4)

# Watermark Text.
watermarkText = Label(text="Water Mark:", font=FONT_NAME, bg="white", highlightthickness=0)
watermarkText.grid(column=0, row=0)

# Watermark Text Field.
watermarkTextField = Entry(width=25)
watermarkTextField.grid(column=1, row=0)
watermarkTextField.insert(0, "@yourWatermarkHere")
watermarkTextField.focus()

# Watermark Button.
watermarkButton = Button(text="Watermark Image", font=(FONT_NAME, 12, "bold"), \
highlightthickness=0, command=watermark)
watermarkButton.grid(column=1, row=4)

# Radio Buttons for Color Choice.
initialSelection = StringVar(value="black")

option1 = Radiobutton(window, text="Black", variable=initialSelection, value="black")
option1.grid(column=0, columnspan=2, row=1)
option2 = Radiobutton(window, text="White", variable=initialSelection, value="white")
option2.grid(column=0, columnspan=2, row=2)
option3 = Radiobutton(window, text="Grey", variable=initialSelection, value="grey")
option3.grid(column=0, columnspan=2, row=3)

# KEEP AT BOTTOM--------
window.mainloop()