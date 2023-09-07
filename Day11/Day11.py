import random
import art
import os

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

def gameStart():
    while True:
        initialPlay = str(input("Do you want to play a game of BlackJack? 'y' for yes, 'n' for no: ")).lower()
        if initialPlay == "n":
            print("Thank you for playing!")
            exit() #--- The exit() funtion will terminate the program.
        elif initialPlay == "y":
            break
        else:
            print("Invalid input. Please try again.")

def dealCards(player, cpu):
    print(art.logo)

    for card in range(2):
        cpu.append(cards[random.randint(0, 12)])
        player.append(cards[random.randint(0, 12)])
    
    if 10 in player and 11 in player:
        player.remove(10)
        player[0] = 0
        print("Player Blackjack")
    
    if 10 in cpu and 11 in cpu:
        cpu.remove(10)
        cpu[0] = 0
        print("CPU Blackjack")


    if cpu[0] == 11 and cpu[1] == 11:
        cpu[1] = 1

    if player[0] == 11 and player[1] == 11:
        player[1] = 1

    playerScore = sum(player)
    cpuScore = sum(cpu)

    print(f"  Your cards: {player}, current score: {playerScore}")
    print(f"  Computer's first card: {cpu[0]}")
    # print(f"  Testing: {cpu} {cpuScore}")

    return player, cpu

def calculateScores(player, cpu):
    playerScore = sum(player)
    cpuScore = sum(cpu)

    if playerScore == 0 or cpuScore == 0:
        return player, cpu

    print(f"  Your final hand: {player}, current score: {playerScore}")
    print(f"  Computer's final hand: {cpu}, final score: {cpuScore}")
    return playerScore, cpuScore

def drawAgain(player, cpu):
    playerScore = sum(player)
    cpuScore = sum(cpu)
    if playerScore == 0 or cpuScore == 0:
        return player, cpu
    
    while True:
        askToDrawAgain = str(input("Type 'y' to get another card, type 'n' to pass: "))
        if askToDrawAgain == "y":
            player.append(cards[random.randint(0, 12)])
            playerScore = sum(player)
        elif askToDrawAgain == "n":
            break
        else:
            print("Invalid input. Please try again.")
        
        if playerScore > 21 and 11 in player:
            found = False
            for ace in range(len(player)):
                if player[ace] == 11 and not found:
                    player[ace] = 1
                    found = True
                    playerScore = sum(player)

        if playerScore > 21:
            break

        print(f"  Your cards: {player}, current score: {playerScore}")
        print(f"  Computer's first card: {cpu[0]}")

    cpuScore = sum(cpu)
    while True:
        if cpuScore < 17:
            cpu.append(cards[random.randint(0, 12)])
            cpuScore = sum(cpu)
        if cpuScore > 21 and 11 in cpu:
            found = False
            for ace in range(len(cpu)):
                if cpu[ace] == 11 and not found:
                    cpu[ace] = 1
                    found = True
            cpuScore = sum(cpu)
        elif cpuScore >= 17:
            break
    return player, cpu

def winStatement(player, cpu):
    playerScore = sum(player)
    cpuScore = sum(cpu)

    if playerScore == cpuScore:
        print("Draw!")
    
    elif playerScore == 0:
        print("You won with a Blackjack!")
    
    elif cpuScore == 0:
        print("CPU got a Blackjack! You lose!")

    elif playerScore > 21 and cpuScore > 21 and playerScore < cpuScore:
        print("You both went over, but dealer has more points so you win!")
    
    elif playerScore > 21 and cpuScore > 21 and playerScore > cpuScore:
        print("You both went over, but dealer has less points so you lose!")
    
    elif playerScore > 21:
        print("You went over. You lose!")

    elif playerScore > cpuScore:
        print("You win!")
    
    elif cpuScore > 21:
        print("Dealer went over. You win!")

    elif cpuScore > playerScore:
        print("You lose!")
#====================================================

playingGame = True
while playingGame == True:
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player = []
    cpu = []
    
    gameStart()

    os.system('cls')

    dealCards(player, cpu)

    drawAgain(player, cpu)

    calculateScores(player, cpu)

    winStatement(player, cpu)


# What teacher wrote.

# import random
# from replit import clear
# from art import logo

# def deal_card():
#   """Returns a random card from the deck."""
#   cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#   card = random.choice(cards)
#   return card

# def calculate_score(cards):
#   """Take a list of cards and return the score calculated from the cards"""

#   if sum(cards) == 21 and len(cards) == 2:
#     return 0
#   if 11 in cards and sum(cards) > 21:
#     cards.remove(11)
#     cards.append(1)
#   return sum(cards)

# def compare(user_score, computer_score):
#   if user_score > 21 and computer_score > 21:
#     return "You went over. You lose 😤"

#   if user_score == computer_score:
#     return "Draw 🙃"
#   elif computer_score == 0:
#     return "Lose, opponent has Blackjack 😱"
#   elif user_score == 0:
#     return "Win with a Blackjack 😎"
#   elif user_score > 21:
#     return "You went over. You lose 😭"
#   elif computer_score > 21:
#     return "Opponent went over. You win 😁"
#   elif user_score > computer_score:
#     return "You win 😃"
#   else:
#     return "You lose 😤"

# def play_game():

#   print(logo)
#   user_cards = []
#   computer_cards = []
#   is_game_over = False

#   for _ in range(2):
#     user_cards.append(deal_card())
#     computer_cards.append(deal_card())

#   while not is_game_over:
#     user_score = calculate_score(user_cards)
#     computer_score = calculate_score(computer_cards)
#     print(f"   Your cards: {user_cards}, current score: {user_score}")
#     print(f"   Computer's first card: {computer_cards[0]}")

#     if user_score == 0 or computer_score == 0 or user_score > 21:
#       is_game_over = True
#     else:
#       user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
#       if user_should_deal == "y":
#         user_cards.append(deal_card())
#       else:
#         is_game_over = True

#   while computer_score != 0 and computer_score < 17:
#     computer_cards.append(deal_card())
#     computer_score = calculate_score(computer_cards)

#   print(f"   Your final hand: {user_cards}, final score: {user_score}")
#   print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
#   print(compare(user_score, computer_score))

# while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
#   clear()
#   play_game()




  # -----Code Graveyard



# def dealCards():
#     os.system('cls')
#     print(art.logo)
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     player = []
#     cpu = []

#     for card in range(2):
#         cpu.append(cards[random.randint(0, 12)])
#         player.append(cards[random.randint(0, 12)])
    
#     if cpu[0] == 11 and cpu[1] == 11:
#         cpu[1] = 1

#     if player[0] == 11 and player[1] == 11:
#         player[1] = 1

#     playerScore = sum(player)
#     cpuScore = sum(cpu)
#     print(f"Your cards: {player}, current score: {playerScore}")
#     print(f"Computer's first card: {cpu[0]}")
#     print(f"{cpu} {cpuScore}")

#     while True:
#         drawCard = str(input("Type 'y' to get another card, type 'n' to pass: ")).lower()
#         if drawCard == "n":
#             print(f"Your final hand: {player}, final score: {playerScore}")
#             break

#         elif drawCard == "y":
#             player.append(cards[random.randint(0, 12)])
#             if playerScore <= 21:
#                 print(f"Your cards: {player}, current score: {playerScore}")
#                 print(f"Computer's first card: {cpu[0]}")

#             else:
#                 break

#         else:
#             print("Invalid input. Please try again.")


# def drawAnotherCard():
#     while True:
#         drawCard = str(input("Type 'y' to get another card, type 'n' to pass: ")).lower()
#         if drawCard == "n":
#             break
#         elif drawCard == "y":
            
#             break
#         else:
#             print("Invalid input. Please try again.")

# while True:
#     askToDrawAgain = str(input("Type 'y' to get another card, type 'n' to pass: "))
#     if askToDrawAgain == "y":
#         playerDrawAgain(player)

#     elif askToDrawAgain == "n":
#         print("Testing")
#         break

#     else:
#         print("Invalid input. Please try again.")

# def computerDrawAgain(cpu, cards):
#     cpuScore = sum(cpu)
#     while True:
#         if cpuScore < 17:
#             cpu.append(cards[random.randint(0, 12)])
#             if cpu[-1] == cards[0] and cpuScore > 17:
#                 cpu[-1] = 1
#             cpuScore = sum(cpu)
#         elif cpuScore >= 17:
#             break
#     return cpu
