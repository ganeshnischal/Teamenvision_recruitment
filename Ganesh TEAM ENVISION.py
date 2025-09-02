"""
Rock, Paper, Scissors Game
--------------------------------------------
How to Play:
- Type "rock", "paper", or "scissors".
- The computer will randomly pick one.
- The winner is decided based on the rules:
  Rock beats Scissors, Scissors beats Paper, Paper beats Rock.
- The game continues until you type "exit".
"""

import random

def play_game():
    player_score = 0
    computer_score = 0

    print("Welcome to Rock, Paper, Scissors!")
    print("Type 'rock', 'paper', or 'scissors' to play.")
    print("Type 'exit' to quit the game.\n")

    while True:
        player_choice = input("Your choice: ").lower()

        if player_choice == "exit":
            break

        if player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please try again.\n")
            continue

        computer_choice = random.choice(["rock", "paper", "scissors"])
        print("Computer choice:"+ computer_choice)
        if player_choice == computer_choice:
            print("It's a draw!\n")
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            print("You win this round!\n")
            player_score += 1
        else:
            print("Computer wins this round!\n")
            computer_score += 1

    print("\nFinal Score:")
    print(f"You: {player_score} | Computer: {computer_score}")
    print("Thanks for playing!")

# Run the game
play_game()