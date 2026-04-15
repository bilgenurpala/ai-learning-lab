# Password Generator

## Rules:

## Ask the user how many letters, symbols and numbers they want in their password
## Create separate lists for letters, symbols and numbers
## Use loops to randomly pick from each list and build the password
## Shuffle the final password so the characters are in random order
## Print the generated password

import random

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbols = '!@#$%^&*()'
numbers = '0123456789'
password = ''
num_letters = int(input("How many letters would you like in your password? "))
num_symbols = int(input("How many symbols would you like in your password? "))
num_numbers = int(input("How many numbers would you like in your password? "))
for _ in range(num_letters):
    password += random.choice(letters)
for _ in range(num_symbols):
    password += random.choice(symbols)
for _ in range(num_numbers):
    password += random.choice(numbers)
password_list = list(password)
random.shuffle(password_list)
final_password = ''.join(password_list)
print(f"Your generated password is: {final_password}")

