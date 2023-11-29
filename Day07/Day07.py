import random
import HangManArt
import HangManWords
import os

# Hangman Project

#Step 1 

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

#Step 2

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

#Step 3

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

# What I wrote up to step 3.

# word_list = ["aardvark", "baboon", "camel"]
# chosenString = random.choice(word_list)
# chosen_word = list(chosenString)
# #Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# display = list("_" * len(chosen_word))
# print(display)

# guess = input('Guess a letter that is in the word: ').lower()
# wordLength = len(chosen_word)

# letterPosition = 0
# for letter in chosen_word:
#     if letter == guess:
#         display[letterPosition] = guess
#         letterPosition += 1
#     else:
#         letterPosition += 1

# print(display)

# #Check guessed letter
# while "_" in display:
#     if "_" in display:
#         guess = input('Guess a letter that is in the word: ').lower()

#     for position in range(wordLength):
#         letter = chosen_word[position]
#         # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
#         if letter == guess:
#             display[position] = letter

#     print(display)
#     if "_" not in display:
#         print(f"You win! The word was: {str(chosenString)}.")

#Step 4
print(HangManArt.logo)
end_of_game = False
chosen_word = random.choice(HangManWords.word_list)
word_length = len(chosen_word)
lives = 6
allGuessedLetters = []

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    # lives = 6
    print(HangManArt.stages[lives])
    print(f"{' '.join(display)}")
    guess = input("Guess a letter: ").lower()
    os.system('cls')

    if guess not in allGuessedLetters:
        allGuessedLetters.append(guess)
    else:
        print(f"You have already guessed {guess}.")
        continue

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
        lives -= 1
        print(f"The letter {guess}, is not in the word.")

    if lives == 0:
        print("You lose!")
        quit()
    #Join all the elements in the list and turn it into a String.
    # print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print(f"You win! The correct word was {str(chosen_word)}.")

    #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
