# Caesar Cipher exercise for Day 8 of 100 days of python code. My complete version.
import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


# Creation of function CAESAR that will take 3 inputs, a direction, a text and a shift.
def caesar(direction: str, text: str, shift: int) -> str:
    """The encrypt function will be used to create a cipher of a given input. It takes 3 arguments:
    1) If you want to encode or decode
    2) Your message
    3) The number for the alphabet forward  or backwards shift
    For example:
    plain_text = 'hello'
    shift = 5
    cipher_text = 'mjqqt'
    print output: 'The encoded text is mjqqt' """

    new_text = ''
    new_shift = shift % 26 if shift > 26 else shift
    print(f'The new shift is {new_shift}')
    for letter in text:

        # Ensure only letters are taking into consideration when ciphering the user input
        index = alphabet.index(letter) if letter in alphabet else -26

        # Depending on user the input message will be encoded or decoded
        if direction == 'encode':
            cipher_index = index + new_shift if index != -26 else index

            # Checks if the shift will move past the last letter of the alphabet so it takes it back from the beginning
            if cipher_index > 25:
                cipher_index = cipher_index - 26

            # New text is created ignoring the symbols or spaces
            new_text += alphabet[cipher_index] if cipher_index != -26 else letter

        elif direction == 'decode':
            decipher_index = index - new_shift if index != -26 else index

            if decipher_index < 0 and decipher_index != -26:
                decipher_index = decipher_index + 26

            new_text += alphabet[decipher_index] if decipher_index != -26 else letter

    print(f"The {direction}d text is {new_text}")


# Variable for the continuation of the loop
go_ahead = 'yes'

while go_ahead == 'yes':
    # User inputs
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # Execution of the function caesar
    caesar(direction, text, shift)

    # Ask user if they want to continue using the program or not
    go_ahead = input('Would you like to decipher something else? (yes/no): ').lower()

else:
    # If user selects 'no' exit the while loop above and greets them good bye
    quit('bye bye')


