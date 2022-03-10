from art import logo

print(logo)


# Functions #

# Addition
def add(n1, n2):
    return n1 + n2


# Subtraction
def subtract(n1, n2):
    return n1 - n2


# Multiplication
def multiply(n1, n2):
    return n1 * n2


# Division
def divide(n1, n2):
    return n1 / n2


# Operators dictionary
calc_dict = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}


def calculator():
    calculating = True

    # Inputs and calculations to start of the calculator
    # First user input
    num1 = float(input("What's the first number? "))
    # Print the available operators
    for symbol in calc_dict:
        print(symbol)
    # Ask the user to choose an operator from above
    user_symbol = input("Chose an operator: ")
    # Second user input
    num2 = float(input("What's the second number? "))
    # Calculate & print the results
    final_ans = calc_dict[user_symbol](num1, num2)
    print(f"{num1} {user_symbol} {num2} = {final_ans}")

    # Keep calculator on until user exits the program
    while calculating:
        cont_calc = input(
            f"Type: \n'y' to continue calculating with {round(final_ans, 3)} \n'n' to exit \n'c' to restart \n-> ")
        if cont_calc == 'y':
            # User inputs
            user_symbol2 = input("Chose an operator: ")
            next_num = float(input("What's the next number? "))
            # New calculation and result
            continued_ans = calc_dict[user_symbol2](final_ans, next_num)
            print(f"{final_ans} {user_symbol2} {next_num} = {continued_ans}")
            # Replace final answer variable with the new answer
            final_ans = continued_ans
        elif cont_calc == 'c':
            calculating = False
            calculator()
        else:
            exit('bye bye')


calculator()

