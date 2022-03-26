# Created By: Antonia Andreou
# Created Date: 22nd February 2022
# Last Revised By: Antonia Andreou
# Last Revised Date: 28th February 2022

# Modules
from resources import income, menu, resources


# Functions


def drink_resources(key: str) -> tuple:
    """
    The function retrieves the resource information for the drink selected from the dictionary called 'menu' from the
    'resource.py' file.
    :param key: a dictionary key from 'menu'
    :return: tuple with resource volumes for the drink selected
    Example:
    >>> drink_resources("latte")
    (200, 150, 24)
    """
    water = menu.get(key, {}).get("ingredients", {}).get("water", 0)
    milk = menu.get(key, {}).get("ingredients", {}).get("milk", 0)
    coffee = menu.get(key, {}).get("ingredients", {}).get("coffee", 0)
    return water, milk, coffee


def machine_resources() -> tuple:
    """
    The function retrieves the latest machine resources.
    :return: tuple with the latest machine resources
    """
    machine_water = resources["water"]
    machine_milk = resources["milk"]
    machine_coffee = resources["coffee"]
    return machine_water, machine_milk, machine_coffee


def machine_resource_check(avail_res: tuple, needed_res: tuple) -> bool:
    """
    The function takes the tuple output of either the 'machine_resources' function and checks that is more or equal
    to the tuple output of the 'drink_resources' function called for the latest drink order.
    :return: a boolean value of True or False
    """
    if all(x >= y for x, y in zip(avail_res, needed_res)):
        return True
    else:
        return False


def machine_resource_update(initial_res: tuple, used_res: tuple):
    """
    The function updates the machine resources for the drink order placed by the user.
    :param initial_res: call of the 'machine_resources' function
    :param used_res: call of the 'drink_resources' function for the drink order
    :return: no return, just update of the existing dictionary
    """
    resources["water"] = initial_res[0] - used_res[0]
    resources["milk"] = initial_res[1] - used_res[1]
    resources["coffee"] = initial_res[2] - used_res[2]


def machine_money(key: str) -> float:
    """
    The function takes the current machine balance, and once a user has entered sufficient funds for their order,
    adds the cost of their order/drink and returns the updated balance.

    :return: float with the latest machine money balance
    """
    current_money = income.get("money")
    drink_cost = menu.get(key, {}).get("cost")
    income["money"] = current_money + drink_cost
    return income["money"]


def machine_report() -> print():
    """
    The function displays a report of the current machine resource and money balance for the user.
    :return: a series of strings creating the machine report
    """
    print("Water: " + str(resources.get("water")) + "ml")
    print("Milk: " + str(resources.get("milk")) + "ml")
    print("Coffee: " + str(resources.get("coffee")) + "g")
    print("Money $" + str(income.get("money")))


def insufficient_resources(avail_res: tuple, needed_res: tuple, drk: str) -> str:
    """
    The function detects which resources are not sufficient for the drink selected and informs the user
    accordingly.
    :return: prints a string indicating which resource has run out.
    """
    try:
        run_out_resources = []
        for x, y in zip(avail_res, needed_res):
            if x < y:
                run_out_resources.extend([list(menu.get(drk, {}).get("ingredients", {}).keys())[needed_res.index(y)]])

        formatted_run_out_resources = " & ".join(run_out_resources).title()
        print(f"Insufficient resources. {formatted_run_out_resources} --> run out.")
    except IndexError:
        print("Insufficient resources")
        exit("Machine turned off")


def drink_action(drk: str):
    """
    The main function of the coffee machine program.
    :return:
    """
    # Check the drink resources against the machine's using the 'machine_resource_check' function.
    machine = machine_resources()
    drink_selected = drink_resources(drk)
    if machine_resource_check(machine, drink_selected) is True:

        # If sufficient resources are in place, ask user to insert money.
        print("Please insert coins:")
        quarters = int(input("How many quarters: "))
        dimes = int(input("How many dimes: "))
        nickles = int(input("How many nickles: "))
        pennies = int(input("How many pennies: "))

        # Calculate the total of the user's coins {quarters: 0.25, dimes: 0.10, nickles: 0.05,
        # pennies: 0.01}
        money_total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
        cost = menu.get(drk, {}).get("cost", 0)

        # If the user inserts too much money then return change and notify them that their drink is ready to enjoy
        if money_total >= cost:
            machine_money(drk)
            machine_resource_update(machine, drink_selected)
            if money_total == cost:
                print(f"Here is your {drk}! Enjoy!!")
            else:
                change = money_total - cost
                print(f"Here is {round(change, 2)} in change.")
                print(f"Here is your {drk}! Enjoy!!")
        else:
            # If not enough money were inserted, notify user and refund them.
            print("Sorry not enough money. Money refunded.")
    else:
        insufficient_resources(machine, drink_selected, drk)


# MAIN

machine_on = True

# While loop in place for the machine to stay on until the user chooses to off it.
while machine_on:
    # Ask the user what they would like to order.
    user_order = int(input("\nWhat would you like? \nMENU: \n1. Espresso - $1.50 \n2. Latte - $2.50 \n3. Cappuccino - "
                           "$3.00 \n4. Machine Information \nInput Number: "))

    if user_order == 1:
        drink = "espresso"
        drink_action(drink)
    elif user_order == 2:
        drink = "latte"
        drink_action(drink)
    elif user_order == 3:
        drink = "cappuccino"
        drink_action(drink)
    elif user_order == 4:
        user_troubleshoot = int(input("Would you like:\n1. A machine report \n2. Machine Shutdown \nInput Number: "))
        # The 'machine_report' function is called in order for the report to be displayed for the user.
        if user_troubleshoot == 1:
            print("report")
            machine_report()
        # The machine is turned off but exiting the while loop and finishing the program.
        elif user_troubleshoot == 2:
            print("Machine is now off. Bye Bye.")
            machine_on = False
        # In case another invalid option is selected then the user is informed the program is restarted.
        else:
            print("ERROR: Invalid input")
    else:
        print("ERROR: Invalid input")





