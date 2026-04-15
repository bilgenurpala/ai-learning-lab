# Rock Paper Scissors Game

## Rules:

## Store ["Rock", "Paper", "Scissors"] in a list
## Use random.choice() to pick the computer's choice
## Ask the user to type their choice
## Compare the two choices and print who wins
## Handle all possible outcomes: Win, Lose, Draw

import random

choices = ["Rock", "Paper", "Scissors"]
computer_choice = random.choice(choices)
user_choice = input("Enter your choice (Rock, Paper, Scissors): ").capitalize()
print(f"Computer chose: {computer_choice}")
if user_choice == computer_choice:
    print("It's a draw!")
elif (user_choice == "Rock" and computer_choice == "Scissors") or \
        (user_choice == "Paper" and computer_choice == "Rock") or \
        (user_choice == "Scissors" and computer_choice == "Paper"):
    print("You win!")
else:
    print("You lose!")
