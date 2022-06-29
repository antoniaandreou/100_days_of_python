import pandas as pd

nato_alphabet = pd.read_csv('nato_phonetic_alphabet.csv')

nato_alphabet_dict = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}

user_input = input("Enter a word: ")

letter_phonetics = [nato_alphabet_dict[letter.upper()] for letter in user_input]
print(letter_phonetics)

