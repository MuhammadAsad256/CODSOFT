# Importing the random module for generating computer choices
import random

# Welcome message
print("~~~~~~~~~~~~Welcome to the Rock-Paper-Scissors Game!~~~~~~~~~~~~")

# Initializing scores and ties
user_score = 0
comp_score = 0
ties = 0

# Asking for the player's name
name = input("Enter Your Name: ")

# Displaying the rules of the game
print("""
    Winning Rules:
1. Paper vs Rock --> Paper
2. Rock vs Scissor --> Rock
3. Scissors vs Paper --> Scissor""")

# Game loop
while True:

    # Displaying the options for the player to choose from
    print("""
Choices are:
    1. Rock
    2. Paper
    3. Scissors""")

    # Asking for the player's choice
    choice = int(input("Enter your choice from 1-3: "))
    print()

    # Validating the player's input
    while choice > 3 or choice < 1:
        choice = int(input("Please enter a valid input: "))

    # Converting the player's choice to a string
    if choice == 1:
        user_choice = "Rock"
    elif choice == 2:
        user_choice = "Paper"    
    else:
        user_choice = "Scissors"

    # Displaying the player's choice
    print("Your choice is:", user_choice)
    print()

    # Generating the computer's choice
    print("Now it's the computer's turn...")
    print()

    computer = random.randint(1,3)

    # Converting the computer's choice to a string
    if computer == 1:
        comp_choice = "Rock"
    elif computer == 2:
        comp_choice = "Paper"    
    else:
        comp_choice = "Scissors"

    # Displaying the computer's choice
    print("The computer's choice is:", comp_choice)

    # Determining the winner and updating scores
    if((user_choice == "Paper" and comp_choice == "Rock") or (comp_choice == "Paper" and user_choice == "Rock")):
        print("Paper Wins")
        result = "Paper"
    elif((user_choice == "Scissors" and comp_choice == "Rock") or (comp_choice == "Scissors" and user_choice == "Rock")):
        print("Rock Wins")
        result = "Rock"
    elif(user_choice == comp_choice):
        print("It's a tie")
        result = "Tie"
    else:
        print("Scissors")
        result = "Scissors"

    
    # Updating scores based on the result
    if result == "Tie":
        ties += 1
    elif result == user_choice:
        print("You win!")
        user_score += 1
    else:
        print("Computer wins!")
        comp_score += 1

    # Displaying scores
    print()
    print("Scores:")
    print(name, "score is", user_score)
    print("Computer's score is", comp_score)
    print("Ties:", ties)

    # Asking if the player wants to play again
    repeat = input("Do you want to play again? (yes/no): ")
    if repeat == "no" or repeat == "No" or repeat == "NO":
        break
    
print("Game over. Thanks for playing!")
