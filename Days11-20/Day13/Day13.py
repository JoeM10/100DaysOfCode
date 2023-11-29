############DEBUGGING#####################

# # Describe Problem
# Before: The function will do nothing since i never makes it to 20.

# def my_function():
#   for i in range(1, 20):  <---###
#     if i == 20:
#       print("You got it")
# my_function()

# After: Changing the range to (1, 21) will fix the issue.

# def my_function():
#   for i in range(1, 21):
#     if i == 20:
#       print("You got it")
# my_function()


# # Reproduce the Bug
# Before: The randint() range is 1-6 but 6 is not a valid index for dice_imgs.
# The first index in dice_imgs wil not be called either since lists start at position 0 and that is not in the randint() range.

# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])

# After: Changing the range for randint to (0, 5), will fix the issue allowing the program to go through the full list of dice_imgs.

# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])


# # Play Computer
# Before: If 1994 was the input then nothing would happen since there is no if statement to catch it.
# The current if statements are for if the input is above 1994 or below 1994 and above 1980, not including 1994 or 1980.

# year = int(input("What's your year of birth? "))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# After: Giving the if statements >= rather than just > will allow the program to function as intended.

# year = int(input("What's your year of birth? "))
# if year >= 1980 and year < 1994:
#   print("You are a millenial.")
# elif year >= 1994:
#   print("You are a Gen Z.")


# # Fix the Errors
# Before: There is multiple issues here. First would be the print statement is not indented correctly.
# Second, input() defaults to being a str, so this causes a TypeError when trying to compare them in the if statement.
# Third, the print statement is not setup correctly. It is supposed to be a f-string but there is not a f to designate it as so.
# Fourth, we want 18 included as a acceptable value to complete the if statement and it currently is not.

# age = input("How old are you? ")
# if age > 18:
# print("You can drive at age {age}.")

# After: Adding proper indentation will fix the first issue.
# Changing age to a int before trying to compare them will fix the TyperError issue.
# Adding a f at the beginning of the inside of the print statement will fix the f-string issue.
# In the if statement, changing the comparison to >= rather than > will include 18 like we wanted.

# age = int(input("How old are you? "))
# if age >= 18:
#   print(f"You can drive at age {age}.")


# #Print is Your Friend
# Before: When running this, the final print statement is always 0.

# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# After: By using print after each variable is updated we can find where the issue begins.
# The problem was with words_per_page, it was == which is a comparison, not a reassignment of values.
# It needed to be = to reassign the value of word_per_page.

# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# print(pages)
# word_per_page = int(input("Number of words per page: "))
# print(word_per_page)
# total_words = pages * word_per_page
# print(total_words)
# Alternate solution: Using print statements at the end will help catch other issues
#   if there is other calculations happening after reassignment.
# print(f"pages = {pages}")
# print(f"word_per_page = {word_per_page}")
# print(total_words)


# #Use a Debugger
# Used: https://pythontutor.com/visualize.html#mode=edit
# Before: In its current state, it prints 26 which is not the intended result.
# b_list.append(new_item) is not in the for loop, so its only appending the last updated variable of new_item.

# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])

# After: Putting b_list.append(new_item) into the for loop will update b_list with updated the variable of new_item everytime it loops,
#   rather than just the last updated variable of new_item.

# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])