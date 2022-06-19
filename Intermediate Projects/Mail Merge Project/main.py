"""
Created By: Antonia Andreou
Created Date: 19-June-2022
Last Edited By: Antonia Andreou
Last Edited Date: 19-June-2022
"""

# Read the names from the invited_names.txt and same into a variable
with open("Input/Names/invited_names.txt") as names:
    names_to_letter = names.readlines()

# In the range of the number of names
for name in range(len(names_to_letter)):
    # open the starting_letter.txt and replace the name from a name in the list
    with open("Input/Letters/starting_letter.txt", mode="r") as letter:
        letter_lines = letter.readlines()
        amended_letter = letter_lines[0].replace('[name]', names_to_letter[name].strip())
    # create a new file with the same name from the list as above and write the amended line
    # plus the rest of the letter lines as read above
    with open(f"Output/ReadyToSend/letter_to_{names_to_letter[name]}.txt", mode="a") as new_letter:
        new_letter.write(f"{amended_letter}")
        for line in letter_lines[1:]:
            new_letter.write(f"{line}")
