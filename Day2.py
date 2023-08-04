'''
# Take a 2 digit number and add the 2 digits.
# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

num1 = int(two_digit_number[0])
num2 = int(two_digit_number[1])

print(num1 + num2)

#Mathematical Operations
# Addition
3 + 5
# Subtraction
5 - 3
# Multiplication
3 * 5
# Division
6 / 3
# Power of
2 ** 5
# Floor Division - Gives you the floor of a number as a int.
8 // 4                             ^ floor is a rounded down whole number.
# Addition of current value
num1 += 1
# Subtraction of current value
num1 -= 1
# Multiplication of current value
num1 *= 2
# Division of current value
num1 /= 2
# Floor of current value---Using floor like this gives you a float if you start with a float.
num1 //= 2              ---But gives you a int if you start with a int.

# BMI Calculator

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

h1 = float(height)
w1 = int(weight)

calc1 = int(w1 / (h1 ** 2))
print(calc1)

# Rounding Numbers
print(round(8 / 3, 2))
#                  ^ is how many decimal places it will round to.
# If there is no decimal place designated, it will round it to a whole number.

# f-strings

# By putting f in front of the string, it will do the conversions for you.
# You use curly braces {} to insert variables.
score = 0
height = 1.8
isWinning = True

print(f"Your score is {score}, Your height is {height}, You are winning is {isWinning}.")

# Your Life in Weeks Project
# Make a program that tells you how many days, weeks and months you have left if you were to live to 90years old.

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
yearsLeft = 90 - int(age)

daysLeft = yearsLeft * 365
weeksLeft = yearsLeft * 52
monthsLeft = yearsLeft * 12

print(f"You have {daysLeft} days, {weeksLeft} weeks, and {monthsLeft} months left.")
'''
# Tip Calculator Project

#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator.")
totalBill = float(input("What was the total bill? $"))

tipSelection = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
percentTip = (tipSelection / 100) + 1

numOfPeople = int(input("How many people to split the bill? "))

eachPersonPays = (totalBill * percentTip) / numOfPeople

finalBill = "{:.2f}".format(eachPersonPays)
#              ^--- In order to get the finalBill to show 2 decimals even if there is only need for 1, you have to use this format equation.
print(f"Each person should pay: ${finalBill}")