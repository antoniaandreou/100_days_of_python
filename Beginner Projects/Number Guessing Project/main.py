# Created By: Antonia Andreou
# Created Date: 17th February 2022
# Last Revised By: Antonia Andreou
# Last Revised Date: 17th February 2022

# Modules
import random
import os
from art import logo

os.system('clear')
print(logo)

# 'secret_no' variable is allocated a random number from 1 to 100 both inclusive.
secret_no = random.randint(1, 100)

# Game introduction.
print("\nWelcome to the number guessing game!\nI am thinking of a number between 1 and 100, want to take a guess?")

# Ask the user to decide the difficulty level and allocate the attempts accordingly.
level = input("Choose a difficulty: type 'easy' or 'hard': ").lower()
if level == 'easy':
  attempts = 10
elif level == 'hard':
  attempts = 5

# Inform the user of the attempts remaining and ask them to take a guess. Guide the user of the direction of the secret number. Game ends when the attempts finish or the user guesses the number, which ever comes first.
while attempts != 0:
  print(f"\nYou have {attempts} attempts remaining to guess the number.")
  user_guess = int(input("Take a guess: "))
  attempts = attempts - 1
  if secret_no > user_guess:
    print("Too low")
  elif secret_no < user_guess:
    print("Too high")
  else:
    print(f"Hooray, you got it!!! The number was {secret_no}")
    break
else:
  print(f"\nYou run out of attempts! You lost! The number was {secret_no}")



