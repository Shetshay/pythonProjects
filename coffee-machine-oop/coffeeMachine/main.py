from menu import MENU
from resources import resources

order = ''
drinkCost = 0.0
profit = 0.0


#TODO CHECK IF RESOURCES ARE SUFFICIENT
def resourceChecker(order):
    if resources["water"] < MENU[order]["ingredients"]["water"]:
        print("Sorry there is not enough water.")
        return False
    if order != "espresso":
        if resources["milk"] < MENU[order]["ingredients"]["milk"]:
            print("Sorry there is not enough milk.")
            return False
    if resources["coffee"] < MENU[order]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee.")
        return False
    else:
        return True

def purchase(order):
    global profit
    quarters = 0.25
    dimes = 0.10
    nickles = 0.05
    pennies = 0.01
    global drinkCost
    quarterTimes = int(input(f"how many quarters?: "))
    dimesTimes = int(input(f"how many dimes?: "))
    nicklesTimes = int(input(f"how many nickles?: "))
    penniesTimes = int(input(f"how many pennies?: "))
    quarters *= quarterTimes
    dimes *= dimesTimes
    nickles *= nicklesTimes
    pennies *= penniesTimes
    total = quarters + dimes + nickles + pennies
    if total < drinkCost: # BUDGET CHECKER
        print("Sorry that's not enough money. Money refunded.")
    if total > drinkCost: #TODO SUBTRACT FROM DICTIONARY
        resources["water"] -= MENU[order]["ingredients"]["water"]
        resources["coffee"] -= MENU[order]["ingredients"]["coffee"]
        if order != 'espresso':
            resources["milk"] -= MENU[order]["ingredients"]["milk"]
        #print(f"You paid: {total}")
        profit += MENU[order]["cost"]
        total -= MENU[order]["cost"]
        total = round(total, 2)
        print(f"Here is ${total} in change.")
        print(f"Enjoy your {order}! ☕")

def orderChooser(order):
    if order == 'espresso':
        return resourceChecker(order)
    elif order == 'latte':
        return resourceChecker(order)
    elif order == 'cappuccino':
        return resourceChecker(order)

def report():
    for key, value in resources.items():
        if key == 'money':
            print("$", end="")
            print(f"{key}: {value}", end="")
        if key == 'water':
            print(f"{key}: {value}", end="")
            print("ml")
        if key == 'milk':
            print(f"{key}: {value}", end="")
            print("ml")
        if key == 'coffee':
            print(f"{key}: {value}", end="")
            print("g")

while order != 'off':
    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order == 'espresso' or order == 'latte' or order == 'cappuccino':
        if orderChooser(order):
            print(f"Please insert coins.")
            drinkCost = MENU[order]["cost"]
            purchase(order)
    else:
        print(f"Please enter a valid option.")
    if order == 'report':
        report()
        print(f"Money: {profit}")


