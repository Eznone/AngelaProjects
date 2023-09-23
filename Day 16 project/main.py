from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

print("What would you like to order?")

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options})")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
    
    print(f"The {drink.name} costs {drink.cost} and the ingredients are {drink.ingredients}")
    if (coffee_maker.is_resource_sufficient(drink)) and (money_machine.make_payment(drink.cost)):
        coffee_maker.make_coffee(drink)