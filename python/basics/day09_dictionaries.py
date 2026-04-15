# Silent Auction

# Look at the flowchart and write a Silent Auction program using dictionaries and loops.
# Rules:

# Ask each bidder for their name and bid amount
# Store all bids in a dictionary as {name: bid}
# After each bid, ask if there are other bidders

# If yes → clear the screen and repeat
# If no → find the highest bid and declare the winner


# Use os module to clear the screen: os.system('cls' if os.name == 'nt' else 'clear')

# import os
# bids = {}
# while True:
#     name = input("What is your name? ")
#     bid = int(input("What is your bid? $"))
#     bids[name] = bid
#     more_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
#     if more_bidders == "no":
#         break
#     os.system('cls' if os.name == 'nt' else 'clear')
# highest_bid = 0
# winner = ""
# for bidder, amount in bids.items():
#     if amount > highest_bid:
#         highest_bid = amount
#         winner = bidder
# print(f"The winner is {winner} with a bid of ${highest_bid}.")

import os

bids = {}

def find_winner(bids):
    winner = max(bids, key=bids.get)
    print(f"The winner is {winner} with a bid of ${bids[winner]}.")

while True:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    bids[name] = bid
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if more_bidders == "no":
        find_winner(bids)
        break
    os.system('cls' if os.name == 'nt' else 'clear')
