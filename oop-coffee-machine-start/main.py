from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
order = ''
machine = MoneyMachine()
menu = Menu()
coffee = CoffeeMaker()

items = menu.get_items() #displays all items

def findItem(nameOfItem):
    # menu.menu is an array of MenuItems in the
    # menu class
    for menuItem in menu.menu:
        if menuItem.name == nameOfItem:
            #print(menuItem.name)
            return menuItem
    return False

def findCost(nameOfItem): # find the cost of the menu.menu item
    for cost in menu.menu:
        if cost.name == nameOfItem:
            return cost.cost # unlike the function above, we want to return the
        # cost when we find the name, since it's in a dictionary, we already have its name already since
        # its name is equal to our choice, then we add .cost at the end to get the cost of the item
    return False

while order != "off": # START PROGRAM
    choice = str(input(f"What would you like? ({items})"))
    if menu.find_drink(choice):
        choiceOfUser = findItem(choice)
        if coffee.is_resource_sufficient(choiceOfUser):
            #total = machine.process_coins() # gets the calculation of cost
            if machine.make_payment(findCost(choice)): # gets your change and does the math
                coffee.make_coffee(choiceOfUser)

    if choice == 'r': # SHOW UPDATES
        machine.report()
        coffee.report()
