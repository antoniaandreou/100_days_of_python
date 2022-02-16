# Created by: Antonia Andreou
# Created Date: 9th February 2022
# Last Revised By: Antonia Andreou
# Last Revised Date: 16th February 2022

# Modules
from art import logo
import random
import os


# Functions
def scores(player: list) -> int:
    """
    Iterate through a list and add each number to return the final score.
    Example:
    >>> cards = [10, 2, 3, 4]
    >>> scores(cards)
    19
    """
    score = 0
    for n in player:
        score = score + n
    return score


def ace_card(cards: list) -> list:
    """
    Find the Ace (11) initially counted as 11 and replace it as 1.
    >>> cards = [4, 10, 11]
    >>> ace_card(cards)
    [4, 10, 1]
    """
    cards = [1 if x == 11 else x for x in cards]
    return cards

def winner(p_score: int, d_score: int) -> str:
    """
    Determine the winner based on the scores.
    'p_score' -> refers to the player score
    'd_score' -> refers to the dealer score
    Examples:
    >>> dealer_score = 23
    >>> player_score = 19
    >>> winner(player_score, dealer_score)
            *** You WIN! ***
    """
    if d_score <= 21:
        if p_score <= 21 and (d_score == p_score):
            print("\n\t\t\t*** It's a draw! ***")
        elif (d_score > p_score) or p_score > 21:
            print("\n\t\t\t*** You lose! ***")
        elif p_score > d_score:
            print("\n\t\t\t*** You Win! ***")
    else:
        if p_score <= 21:
            if (p_score > d_score) or d_score > 21:
                print("\n\t\t\t*** You WIN! ***")
        else:
            print("\n\t\t\t*** You BOTH lost! ***")


def current_cards(p_cards: list, p_score: int, d_cards: list) -> str:
    """
    'p_cards' refers to the player's cards list
    'p_score' refers to the player's score from the card list above
    'd_cards' refers to the dealer's cards list
    """
    return f"\tYour cards: {p_cards}, current score {p_score}" f"\n\tDealer's first card: {d_cards[0]}"


def final_cards(p_cards: list, p_score: int, d_cards: list, d_score: int):
    """
    'p_cards' refers to the player's cards list
    'p_score' refers to the player's score from the card list above
    'd_cards' refers to the dealer's cards list
    'd_score' refers to the dealer's score from the card list above
    """
    return f"\tYou final cards {p_cards}, your final score {p_score}" f"\n\tDealer's final cards {d_cards}, Dealer's final score {d_score}"


def blackjack():
    """
    The main function for the Blackjack game.
    Game Rules:
      The deck is unlimited in size.
      There are no jokers.
      The Jack/Queen/King all count as 10.
      The the Ace can count as 11 or 1.
      The cards in the list have equal probability of being drawn.
      Cards are not removed from the deck as they are drawn.
      The computer is the dealer.
    Scores are calculated using the 'scores' function.
    Initial results are displayed using the 'current_cards' function.
    Final results are displayed using the 'final_cards' function. 
    Winner is determined using the 'winner' function.
    """
    # List of card values. 
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    # Empty lists for players.
    dealer = []
    player = []

    # Allocate 2 random cards for player and dealer.
    dealer.extend(random.sample(cards, 2))
    player.extend(random.sample(cards, 2))

    # Calculate the current scores using the 'scores' function.
    player_score = scores(player)
    dealer_score = scores(dealer)
    
    # Return the appropriate information to the player using 'current_cards' function.
    print(current_cards(player, player_score, dealer))

    # If blackjack is achieved from the beginning display final scores and declare the winner accordingly.
    if dealer_score == 21 or player_score == 21:
        print(final_cards(player, player_score, dealer, dealer_score))
        if dealer_score == 21:
            print("\n\t\t\t*** You lose. Dealer has Blackjack!! ***")
            return
        else:
            print("\n\t\t\t*** You win! You have blackjack!! ***")
            return

    # Allow the user to add cards until the score exceeds 21 or user passes. Adjust ace value accordingly.
    player_continues = True
    while player_continues:
        if player_score > 21:
            player_continues = False
        elif input("Type 'y' to get another card, or 'n' to pass:  ").lower(
        ) == 'y':
            player.extend(random.sample(cards, 1))
            player_score = scores(player)
            if player_score > 21 and any(a == 11 for a in player):
                player = ace_card(player)
                player_score = scores(player)
            print(current_cards(player, player_score, dealer))
        else:
            player_continues = False

    # Add more cards for computer until score exceeds 16. Adjust ace value accordingly.
    dealer_continues = True
    while dealer_continues:
        if dealer_score > 16:
            dealer_continues = False
        else:
            dealer.extend(random.sample(cards, 1))
            dealer_score = scores(dealer)
            if dealer_score > 21 and any(a == 11 for a in dealer):
                dealer = ace_card(dealer)
                dealer_score = scores(dealer)

    # # Determine the winner by calling the 'winner' function.
    winner(player_score, dealer_score)

    # Present final cards and scores for both using function 'final_cards'.
    print("\n" + final_cards(player, player_score, dealer, dealer_score))


# Main Body

program_active = True

while program_active:
    if input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': "
             ).lower() == 'y':
        os.system('clear')
        print(logo)
        blackjack()
    else:
        program_active = False
