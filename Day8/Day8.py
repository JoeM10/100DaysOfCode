import math
import art
'''
#                   v --- Parameter
# def greetWithName(name):
#     print(f"Hello {name}.")
#     print(f"How do you do {name}?")

# greetWithName("Tabitha")
#                  ^ --- Argument
# In this example, name is the parameter, and Tabitha is the argument.

# Functions with more than 1 input.
def greetWith(name, location):
    print(f"Hello, {name}.")
    print(f"What is it like in {location}?")
greetWith("Kris", "Germany")

# You can add keyword arguments to function parameters.
# ex: greetWith(name="Kris", location="Germany")
# This will allow you to move the order of the arguments inside the called function without changing the parameter order.
# ex: greetWith(location="Germany", name="Kris") will still function as normal.

# 
# Paint Area Calculator
# 

#Write your code below this line 👇
def paint_calc(height, width, cover):
    calculation = math.ceil((height * width) / cover)
    print(f"You'll need {calculation} cans of paint.")

#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
'''
# 
# Prime Number Checker
# 
'''
#Write your code below this line 👇
# What I wrote, does not work completely:

# You can put things onto another line with \ so they arent so long.

def prime_checker(number):
    if number == 2\
        or number == 3\
        or number == 5:
        print("It's a prime number.")
    else:
        if number % 2 == 0:
            print("It's not a prime number.")
        elif number % 3 == 0:
            print("It's not a prime number.")
        else:
            print("It's a prime number.")

# What Teacher wrote:

def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

# What Jacob and I wrote:
# def prime_checker(number):
#     is_prime = True
#     for i in range(2, int(number/2)):
#         if number % i == 0:
#             is_prime = False
#     if is_prime:
#         print("It's a prime number.")
#     else:
#         print("It's not a prime number.")

#Write your code above this line 👆   
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
'''
# 
# Caeser Cypher Project
# 
def encryption(text:str, shift:int):
    start = ord('a')
    newWord = ""
    for letter in text:
        if letter.isalpha():
            if direction == "decode":
                encryptedChar = chr((ord(letter) - start - shift) % 26 + start)
            else:
                encryptedChar = chr((ord(letter) - start + shift) % 26 + start)
            newWord += encryptedChar
        else:
            newWord += letter
    print(f"The {direction}d text is {newWord}.")

print(art.logo)
restart = False
while restart == False:
    while True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        if direction == "encode" or direction == "decode":
            break
        else:
            print("Invalid input, Please try again.")

    text = input("Type your message:\n").lower()

    while True:
        shift = input("Type the shift number:\n")
        if shift.isdigit():
            shift = int(shift)
            break
        else:
            print("Invalid input. Please type a number.")

    encryption(text, shift)
    while True:
        goAgain = input("Do you want to run the program again? 'yes' or 'no'\n")
        if goAgain == "no":
            print("Goodbye.")
            restart = True
            break
        elif goAgain == "yes":
            break
        else:
            print("Invalid input, please type 'yes' or 'no'.")