# Hangman Game

## Rules:

## Create a word list and pick a random word using random.choice()
## Generate blanks (_) as many as the letters in the word
## Ask the user to guess a letter in a loop
## If the guessed letter is in the word → replace the corresponding blank(s) with the letter
## If the guessed letter is not in the word → lose a life (start with 6 lives)
## Game ends when:

## All blanks are filled → You Win!
## Lives run out → Game Over!

## Print the current state of the word and remaining lives after each guess

## Example output:
## Word: _ _ _ _ _
## Guess a letter: a
## Word: _ a _ _ _
## Lives remaining: 6,

import random

word_list = ["python", "hangman", "programming", "challenge", "developer"]
chosen_word = random.choice(word_list)
display = ['_'] * len(chosen_word)
lives = 6
guessed_letters = []

print("Welcome to Hangman!")

while lives > 0 and '_' in display:
    print(f"Word: {' '.join(display)}")
    guess = input("Guess a letter: ").lower()
    
    if guess in guessed_letters:
        print("You already guessed that letter!")
    elif guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                display[index] = guess
        guessed_letters.append(guess)
    else:
        lives -= 1
        guessed_letters.append(guess)
        print(f"Wrong guess! Lives remaining: {lives}")

if '_' not in display:
    print(f"Congratulations! You guessed the word: {chosen_word}")
else:
    print(f"Game Over! The word was: {chosen_word}")
