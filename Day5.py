import random
'''
# Average Height Calculator Project

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
# You cannot use the len() or sum() function for this exercise.
# Write your code below this row 👇

total = 0
idx = 0
for height in student_heights:
  total += height

for idx, item in enumerate(student_heights):
    idx += 1

averageHeight = round(total / idx)
print(averageHeight)

# 
# Highest Score Project
# 

# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆
# You cannot use the max() or min() function for this exercise.
# Write your code below this row 👇
highScore = 0
for n in student_scores:
  if highScore < n:
    highScore = n
print(f"The highest score in the class is: {highScore}")

# 
# for loop with range and step
#           Start --v      v-- Step
for number in range(1, 11, 2):
#                      ^-- End, does not include ending number.
    print(number)

total = 0
for number in range(1, 101):
    total += number
print(total)

# 
# Adding Even Numbers Project
# 

# Add the even numbers between 1 and 100 including 100.
total = 0
for n in range(0, 101, 2):
    total += n
print(total)

# 
# FizzBuzz Game Project
# 

# You are going to write a program that automatically prints the solution to the FizzBuzz game.
# Your program should print each number from 1 to 100 in turn.
# When the number is divisible by 3 then instead of printing the number it should print "Fizz".
# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
#   And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    
    elif n % 3 == 0:
        print("Fizz")
    
    elif n % 5 == 0:
        print("Buzz")
    
    else:
        print(n)
'''
# 
# Random Password Generator
# 

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

goodUserInput = False
print("Welcome to the PyPassword Generator!")
while not goodUserInput:
    try:
        nr_letters= int(input("How many letters would you like in your password?\n")) 
        nr_symbols = int(input(f"How many symbols would you like?\n"))
        nr_numbers = int(input(f"How many numbers would you like?\n"))
        goodUserInput = True
    except:
        print("Invalid input, please try again.")

password = []

for randLetters in range(nr_letters):
    password += random.choice(letters)

for randSymbols in range(nr_symbols):
    password += random.choice(symbols)

for randNumbers in range(nr_numbers):
    password += random.choice(numbers)

random.shuffle(password)
# print(password) # Outputs a list.

# We are using the code below to turn the list back into a string.
# If you want the for loop to go through the whole list, you dont need to define a start and end.
# char in this case is each item in the list(password) starting at position[0],
#   then on and on until the end of the list.
#   If position[0] in the list is "G", then char = "G" until the next iteration. 
# So each time it iterates through the list(password) it goes onto the next item in the list automatically.
shuffledPassword = ""

for char in password:
    shuffledPassword += char

print(f"Your new password is: {shuffledPassword}")