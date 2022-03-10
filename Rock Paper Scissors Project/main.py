rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
import random
import sys

# Get the user's choice and allocate into a variable
user_choice = int(input("\n\nWhat do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))

if user_choice == 0:
    print(rock)
    user_choice_name = 'rock'
elif user_choice == 1:
    print(paper)
    user_choice_name = 'paper'
elif user_choice == 2:
    print(scissors)
    user_choice_name = 'scissors'
else:
    sys.exit('Invalid Choice')

# Get the computer to generate its choice for the game and allocate into a variable
computer_choice = random.randint(0, 2)

print("\nComputer chose:\n")

if computer_choice == 0:
    print(rock)
    computer_choice_name = 'rock'
elif computer_choice == 1:
    print(paper)
    computer_choice_name = 'paper'
else:
    print(scissors)
    computer_choice_name = 'scissors'

# Create an IF statement to decide the winner of the game.

if computer_choice_name == user_choice_name:
    print("It's a draw!")
elif user_choice_name == 'paper' and computer_choice_name == 'rock':
    print('You win!')
elif user_choice_name == 'rock' and computer_choice_name == 'scissors':
    print('You win!')
elif user_choice_name == 'scissors' and computer_choice_name == 'paper':
    print('You win!')
else:
    print('You lose!')