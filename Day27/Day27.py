from tkinter import *

# # Unlimited Arguments.
# #       |--- The * collects all of the arguments as a tuple.
# #       V  v--- args can be anything but is typically args.
# def add(*args):
#   sum = 0
#   for n in args:
#     sum += n
#   return sum
# print(add(1, 2, 3))

# # kwargs is Key Word Arguments.
# def calculate(n, **kwargs):
#   print(kwargs)
#   # for key, value in kwargs.items():
#     # print(key)
#     # print(value)
#   # print(kwargs["add"])
#   n += kwargs["add"]
#   n *= kwargs["multiply"]
# calculate(2, add=3, multiply=5)

# class Car:
#   def __init__(self, **kw):
#     #               V--- .get() will return none if you dont use it, rather than giving a error.
#     self.make = kw.get("make")
#     self.model = kw.get("model")

# myCar = Car(make="Nissan", model="GT-R")
# print(myCar.make)
# print(myCar.model)

# Notes--------

# #Creating a new window and configurations
# window = Tk()
# window.title("Widget Examples")
# window.minsize(width=500, height=500)

# #Labels
# label = Label(text="This is old text")
# label.config(text="This is new text")
# label.pack()

# #Buttons
# def action():
#     print("Do something")

# #calls action() when pressed
# button = Button(text="Click Me", command=action)
# button.pack()

# #Entries
# entry = Entry(width=30)
# #Add some text to begin with
# entry.insert(END, string="Some text to begin with.")
# #Gets text in entry
# print(entry.get())
# entry.pack()

# #Text
# text = Text(height=5, width=30)
# #Puts cursor in textbox.
# text.focus()
# #Adds some text to begin with.
# text.insert(END, "Example of multi-line text entry.")
# #Get's current value in textbox at line 1, character 0
# print(text.get("1.0", END))
# text.pack()

# #Spinbox
# def spinbox_used():
#     #gets the current value in spinbox.
#     print(spinbox.get())
# spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()

# #Scale
# #Called with current scale value.
# def scale_used(value):
#     print(value)
# scale = Scale(from_=0, to=100, command=scale_used)
# scale.pack()

# #Checkbutton
# def checkbutton_used():
#     #Prints 1 if On button checked, otherwise 0.
#     print(checked_state.get())
# #variable to hold on to checked state, 0 is off, 1 is on.
# checked_state = IntVar()
# checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
# checked_state.get()
# checkbutton.pack()

# #Radiobutton
# def radio_used():
#     print(radio_state.get())
# #Variable to hold on to which radio button value is checked.
# radio_state = IntVar()
# radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
# radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()


# #Listbox
# def listbox_used(event):
#     # Gets current selection from listbox
#     print(listbox.get(listbox.curselection()))

# listbox = Listbox(height=4)
# fruits = ["Apple", "Pear", "Orange", "Banana"]
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()

# #Keep at bottom
# window.mainloop()

def buttonClicked():
  print("I got clicked")
  newText = input.get()
  myLabel.config(text=newText)

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=500)
window.config(padx=20, pady=20) #-------- Adds space around the edge of the window. Can be used on widgets as well.

#Label
myLabel = Label(text="I Am a Label", font=("Arial", 24, "bold"))
myLabel.config(text="New Text")
# myLabel.pack() #-------- .pack() can be difficult to position things in specific spots.
# myLabel.place(x=0, y=0) #-------- .place() can be used for specific placement.
myLabel.grid(column=0, row=0) #-------- .grid() can be used when precise placement isnt neccessary, but still offers greater positioning than .pack().
# .grid() and .pack() cannot both be used in the same code. One or the other must be chosen.

#Button1
button1 = Button(text="Click Me", command=buttonClicked)
button1.grid(column=1, row=1)

#Button2
button2 = Button(text="No, Click Me", command=buttonClicked)
button2.grid(column=2, row=0)

#Entry
input = Entry(width=30)
print(input.get())
input.grid(column=3, row=2)

#Keep at bottom
window.mainloop()