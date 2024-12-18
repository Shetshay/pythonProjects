from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
order = ''
machine = MoneyMachine()
menu = Menu()
coffee = CoffeeMaker()
drink = 0.0 # SET TO FLOAT
items = menu.get_items() # VARIABLE TO DISPLAY ALL ITEMS
while order != "off": # START PROGRAM
    choice = str(input(f"What would you like? ({items})"))
    drinkChosen = menu.find_drink(choice) #THE DRINK WE CHOSE, IS IN THIS OBJECT VARIABLE
    if menu.find_drink(choice): # IF THE DRINK THEY CHOSE IS IN THE MENU
        if coffee.is_resource_sufficient(menu.find_drink(choice)): # IF THERE IS ENOUGH RESOURCES
            # TO MAKE THIS OBJECT  & IT FOUND THE DRINK IN THE MENU
            for item in menu.menu: # GO THROUGH THE MENU AND IF DRINK CHOSEN = AN ITEM ON THE MENU
                if item == drinkChosen:
                    drink = item.cost # SET DRINK TO THE COST OF THE DRINK
                    #print(drink)
            if machine.make_payment(drink): # gets your change and does the math
                coffee.make_coffee(drinkChosen)
    if choice == 'r': # SHOW UPDATES
        machine.report()
        coffee.report()
