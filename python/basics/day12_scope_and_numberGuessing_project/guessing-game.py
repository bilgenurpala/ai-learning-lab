import random

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return 10
    else:
        return 5

def check_answer(guess, answer, lives):
    if guess > answer:
        print("Too high!")
        return lives - 1
    elif guess < answer:
        print("Too low!")
        return lives - 1
    else:
        print(f"You got it! The answer was {answer}.")
        return lives

def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)
    lives = set_difficulty()
    guess = 0

    while guess != answer:
        print(f"You have {lives} attempts remaining.")
        guess = int(input("Make a guess: "))
        lives = check_answer(guess, answer, lives)
        if lives == 0:
            print("You've run out of guesses. You lose!")
            return

game()
while input("Do you want to play again? Type 'yes' or 'no': ").lower() == "yes":
    game()
