# The rules follow the classic “Rock Paper Scissors” game, but with two new choices – “Lizard” and “Spock”:

# Scissors cut Paper.
# Paper covers Rock.
# Rock crushes Lizard.
# Lizard poisons Spock.
# Spock smashes Scissors.
# Scissors beat Lizard.
# Lizard eats Paper.
# Paper disproves Spock.
# Spock vaporizes Rock.
# Rock breaks Scissors.
# Watch this video to understand it better.

# Here's a note from the creator, Sam Kass:

# “I invented this game because it seems like when you know someone well enough, 75-80% of any Rock Paper Scissors games you play with that person end up in a tie. Well, here is a slight variation that reduces that probability. This version is also nice because it satisfies the Law of Fives.”

# Go back to your Rock Paper Scissors program and turn it into Rock Paper Scissors Lizard Spock!

# Use '🖖' for "Spock" and '🦎' for "Lizard".

# The output should look something like this:

# ================================
# Rock Paper Scissors Lizard Spock
# ================================

# 1) ✊
# 2) ✋
# 3) ✌️
# 4) 🦎
# 5) 🖖
# Pick a number: 3

# You chose: ✌️
# CPU chose: ✌️
# It's a tie!

import random
print("==============================")
print("Rock Paper Scissors Lizard Spock")
print("==============================")
print("1) ✊")
print("2) ✋")
print("3) ✌️")
print("4) 🦎")
print("5) 🖖")

choices = ["✊", "✋", "✌️", "🦎", "🖖"]
user_choice = int(input("Pick a number: "))
cpu_choice = random.choice(choices)
print(f"\nYou chose: {choices[user_choice - 1]}")
print(f"CPU chose: {cpu_choice}")

if user_choice == 1:  
    if cpu_choice in ["✌️", "🦎"]:
        print("You win!")
    elif cpu_choice in ["✋", "🖖"]:
        print("CPU wins!")
    else:
        print("It's a tie!")
elif user_choice == 2:  
    if cpu_choice in ["✊", "🖖"]:
        print("You win!")
    elif cpu_choice in ["✌️", "🦎"]:
        print("CPU wins!")
    else:
        print("It's a tie!")
elif user_choice == 3:  
    if cpu_choice in ["✋", "🦎"]:
        print("You win!")
    elif cpu_choice in ["✊", "🖖"]:
        print("CPU wins!")
    else:
        print("It's a tie!")
elif user_choice == 4:  
    if cpu_choice in ["✋", "🖖"]:
        print("You win!")
    elif cpu_choice in ["✊", "✌️"]:
        print("CPU wins!")
    else:
        print("It's a tie!")
elif user_choice == 5:  
    if cpu_choice in ["✊", "✌️"]:
        print("You win!")
    elif cpu_choice in ["✋", "🦎"]:
        print("CPU wins!")
    else:
        print("It's a tie!")
else:
    print("Invalid choice! Please pick a number between 1 and 5.")