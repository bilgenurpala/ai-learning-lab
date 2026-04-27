import random
from game_data import data
from art import logo, vs

def format_account(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description} from {country}"

def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"
    
score = 0
game_should_continue = True
account_b = random.choice(data)

print(logo)

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)
    print(f"Compare A: {format_account(account_a)}.")
    print(vs)
    print(f"Against B: {format_account(account_b)}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    print("\n" * 20)
    print(logo)

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}.")