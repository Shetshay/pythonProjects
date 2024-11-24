from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
order = ''
machine = MoneyMachine()
menu = Menu()
coffee = CoffeeMaker()

#choice = MenuItem()

items = menu.get_items() #displays all items

while order != "off":
    choice = input(f"What would you like? ({items})")
    if menu.find_drink(choice):
        if coffee.is_resource_sufficient(choice):
            total = machine.process_coins() # gets the calculation of cost
            machine.make_payment(total) # gets your change and does the math
    if choice == 'r':
        machine.report()
        coffee.report()
