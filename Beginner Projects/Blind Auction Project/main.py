from replit import clear
from art import logo

print(logo)

# Create an empty dictionary to store user information and bids.
auction_dict = {}

# While state is True then the while loop below will keep taking in bids from users.
state = True

# Start program to collect bids.
while state is True:

    name = input("What is your name: ").title()
    bid = int(input("How much do you want to bid? £"))

    # Add record to the auction dictionary.
    auction_dict[name] = bid

    # Ask if there are more users. If no more bids then turn state to False to exit while loop.
    more_bids = input("Is someone else bidding? (yes/no): ").lower()
    clear()
    if more_bids == "no":
        state = False

# Go through the dictionary and retrieve user with max bid.
winner = max(auction_dict, key=auction_dict.get)

# Declare the winner alongside their bid.
print(f"The winner of this auction is {winner} with a bid of {auction_dict[winner]}")
