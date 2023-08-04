import random
'''
# Prints a random integer within the parameters given.
randomInteger = random.randint(1, 10) #both included
print(randomInteger)

# Prints a random float between 0 and 1 but not including 1.
randomFloat = random.random()
print(randomFloat)

#
# Heads or Tails project.
#

coinToss = random.randint(0, 1)

if coinToss == 0:
    print("Heads")
else:
    print("Tails")

#

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", 
                     "Connecticut", "Massachusetts", "Maryland", "South Carolina", 
                     "New Hampshire", "Virginia", "New York", "North Carolina", 
                     "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", 
                     "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", 
                     "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", 
                     "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", 
                     "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", 
                     "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", 
                     "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america[0])
#                       ^ -- This number is the position in the list. You can use - to start from the end of a list, -1 is the last item.

# You can change each item in the list individually.
states_of_america[1] = "Pencilvania"

# You can add items into the list by using .append
states_of_america.append("TabiTown")

# You can use .extend to take another list and add it onto a existing list.
states_of_america.extend(["GeorgeWorld", "Scooblandia"])
'''
'''
---Source--- https://docs.python.org/3/tutorial/datastructures.html

list.append(x)
Add an item to the end of the list. Equivalent to a[len(a):] = [x].

list.extend(iterable)
Extend the list by appending all the items from the iterable. Equivalent to a[len(a):] = iterable.

list.insert(i, x)
Insert an item at a given position.
The first argument is the index of the element before which to insert,
so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).

list.remove(x)
Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.

list.pop([i])
Remove the item at the given position in the list, and return it.
If no index is specified, a.pop() removes and returns the last item in the list.
(The square brackets around the i in the method signature denote that the parameter is optional, not that you should type square brackets at that position.
You will see this notation frequently in the Python Library Reference.)

list.clear()
Remove all items from the list. Equivalent to del a[:].

list.index(x[, start[, end]])
Return zero-based index in the list of the first item whose value is equal to x. Raises a ValueError if there is no such item.

The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list.
The returned index is computed relative to the beginning of the full sequence rather than the start argument.

list.count(x)
Return the number of times x appears in the list.

list.sort(*, key=None, reverse=False)
Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).

list.reverse()
Reverse the elements of the list in place.

list.copy()
Return a shallow copy of the list. Equivalent to a[:]
'''
#
# Banker Roulette Project
# 
'''
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆
# You cannot use .choice for this exercise.
# Write your code below this line 👇
numOfNames = len(names)

randPerson = random.randint(0, numOfNames - 1)

billPayer = names[randPerson]

print(f"{billPayer} is going to buy the meal today!")

# With .choice
personWhoWillPay = random.choice(names) #--- random.choice() will allow you to pick a random item from a list.
print(personWhoWillPay + " is going to buy the meal today!")

#

# You can nest lists inside each other.
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirtyDozen = [fruits, vegetables]

# 
# Treasure Map Challenge
#

# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
vertical = int(position[1])-1
horizontal = int(position[0])-1

map[vertical][horizontal] = "X"
#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
'''
# 
# Rock Paper Scissors Game
# 

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
selections = [rock, paper, scissors]
print("Ready for a game of Rock, Paper, Scissors?\n")
playerSelection = int(input('Type 0 for Rock, 1 for Paper, or 2 for Scissors to play.\n'))

if playerSelection >= 3 or playerSelection < 0:
    print("Invalid input.")
    quit()
else:
    print(selections[playerSelection])

    print("Computer chose:")
    computer = random.randint(0, 2)
    print(selections[computer])

    if playerSelection == 0 and computer == 0: # Rock vs Rock
        print("It was a tie!")

    elif playerSelection == 0 and computer == 1: # Rock vs Paper
        print("You Lose!")

    elif playerSelection == 0 and computer == 2: # Rock vs Scissors
        print("You win!")

    elif playerSelection == 1 and computer == 0: # Paper vs Rock
        print("You win!")

    elif playerSelection == 1 and computer == 1: # Paper vs Paper
        print("It was a tie!")

    elif playerSelection == 1 and computer == 2: # Paper vs Scissors
        print("You lose!")

    elif playerSelection == 2 and computer == 0: # Scissors vs Rock
        print("You lose!")

    elif playerSelection == 2 and computer == 1: # Scissors vs Paper
        print("You win!")

    elif playerSelection == 2 and computer == 2: # Scissors vs Scissors
        print("It was a tie!")
