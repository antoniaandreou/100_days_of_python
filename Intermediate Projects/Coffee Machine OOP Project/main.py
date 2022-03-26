from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()

# coffee_maker is a VARIABLE where the OBJECT created by the CoffeeMaker() CLASS is stored
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

machine_on = True
while machine_on:

    drink_choice = input(f"What would you like? ({menu.get_items()}): ")

    if drink_choice in ["latte", "espresso","cappuccino"]:
        drink_info = menu.find_drink(drink_choice)
        if coffee_maker.is_resource_sufficient(drink_info):
            if money_machine.make_payment(drink_info.cost):
                coffee_maker.make_coffee(drink_info)
    elif drink_choice == "off":
        machine_on = False
    elif drink_choice == "report":
        coffee_maker.report()
        money_machine.report()



