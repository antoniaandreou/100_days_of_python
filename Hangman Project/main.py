# My version of the Hangman Game created for Day 7 of the 100 days of python course.

# Module
import random
import hangman_words
import hangman_art

# Game logo
print(hangman_art.logo)

# A list of words for the game held in module hangman_words.py where one chosen at random is allocated to a variable 'chosen_word'.
chosen_word = random.choice(hangman_words.word_list)

# Setting a variable named lives to track the player's wrong answers.
lives = 6

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# An empty list called display that will hold empty spaces the length of the chosen word.
display = []
for letter in range(len(chosen_word)):
    display.append('_')

# Empty list to file all the wrong guesses
wrong_guesses = []

# While there are blanks ('_') keep asking the user for letters.
while '_' in display and lives > 0:
    guess = input("Guess a letter: ").lower()

    # If the letter was already guessed, let the player know.
    if guess in display or guess in wrong_guesses:
        print(f"You have already guessed {guess}")

    # Loop through the chosen_word to check if the letter the user guessed is part of the word. If so, replace the blanks with the letter(s).
    for i, letter in enumerate(chosen_word):
        if letter == guess:
            display.pop(i)
            display.insert(i, letter)

    # If the letter provided in not part of the chosen word, remove a life from the total & print the equivalent hangman art.
    if guess not in list(chosen_word) and guess not in wrong_guesses:
        # Add the wrong guess to the respective list.
        wrong_guesses.append(guess)

        print(f"{guess} is not part of the word. You lose a life.")
        lives = lives - 1
        print(hangman_art.stages[lives])

    # Print an updated version of the chosen word.
    print(f"{''.join(display)}")

# Print the result
if lives == 0:
    print('You lost!')
else:
    print('You won!')
