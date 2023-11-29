'''
# 
# Functions with outputs.
# 

def formatName(fName, lName):
    """Take a first and last name to format it
    to return the title case version of the name."""
    #^^^ This is called a Docstring. It is used to describe the function for us humans.

    fName = fName.title() #--- The .title() function is used to capitalize only the first letter of each word in a string.
    lName = lName.title() #--- It will also make all other letters lowercase.
    print(fName + " " + lName)

firstName = input("Type your first name.\n")
lastName = input("Type your last name.\n")

formatName(firstName, lastName)

# 
# Days in Month Exercise.
# 

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        # print("Leap year.")
        return True
      else:
        # print("Not leap year.")
        return False
    else:
    #   print("Leap year.")
      return True
  else:
    # print("Not leap year.")
    return False
  
# What I wrote.
def days_in_month(year, month):
  leapBoolean = is_leap(year)
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if leapBoolean == True:
    month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = month_days[month-1]
    return day
  else:
    day = month_days[month-1]
    return day

# What the teacher wrote.
def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  #--- Since is_leap(year) is a Boolean, it will only do the if statement if it is True.
  if is_leap(year) and month == 2:
    return 29
  return month_days[month-1]

# Both answers give the same result.

#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
'''
# 
# Calculator Program
# 

import art
print(art.logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}
# What I wrote for step 1.
# num1 = int(input("What's the first number?: "))
# num2 = int(input("What's the second number?: "))

# for symbol in operations:
#     print(symbol)

# while True:
#   operation_symbol = input("Pick an operation from the line above:")
#   if operation_symbol == "+":
#       answer = add(num1, num2)
#       break

#   elif operation_symbol == "-":
#       answer = subtract(num1, num2)
#       break

#   elif operation_symbol == "*":
#       answer = multiply(num1, num2)
#       break

#   elif operation_symbol == "/":
#       answer = divide(num1, num2)
#       break

#   else:
#       print("Invalid input. Please try again.")

# print(f"{num1} {operation_symbol} {num2} = {answer}")

# # What the teacher wrote for step 1.
# num1 = int(input("What's the first number?: "))
# for symbol in operations:
#     print(symbol)
# operation_symbol = input("Pick an operation from the line above: ")
# num2 = int(input("what's the second number?: "))
# calculation_function = operations[operation_symbol]
# first_answer = calculation_function(num1, num2)

# print(f"{num1} {operation_symbol} {num2} = {first_answer}")

# # Step 2.
# operation_symbol = input("Pick another operation: ")
# num3 = int(input("What's the next number?: "))
# calculation_function = operations[operation_symbol]
# second_answer = calculation_function(first_answer, num3)

# print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")

# Step 3.
num1 = float(input("What's the first number?: "))
for symbol in operations:
    print(symbol)

calculating = True
while calculating == True:
  operation_symbol = input("Pick an operation: ")
  num2 = float(input("what's the next number?: "))
  calculation_function = operations[operation_symbol]
  first_answer = calculation_function(num1, num2)

  print(f"{num1} {operation_symbol} {num2} = {first_answer}")
  while True:
    calcAgain = str(input(f"Type 'y' to continue calculating with {first_answer}, or type 'n' to exit: "))

    if calcAgain == "n":
        calculating = False
        break
    
    elif calcAgain == "y":
        num1 = first_answer
        break

    else:
      print("Invalid answer.")       

# Having a function call itself is called recursion.