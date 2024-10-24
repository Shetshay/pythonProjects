from menu import MENU
from resources import resources

order = ''
drinkCost = 0.0
profit = 0.0

quarters = 0.25
dimes = 0.10
nickles = 0.05
pennies = 0.01

#TODO STORE ORDER TYPE
#TODO OFF ENDS THE PROGRAM
#TODO CHECK IF RESOURCES ARE SUFFICIENT

def purchase():
    global quarters
    global dimes
    global nickles
    global pennies
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
    if total < drinkCost:
        print("Sorry that's not enough money. Money refunded.")
    print(total)



def orderChooser(order):
    if order == 'espresso':
        return order
    elif order == 'latte':
        return order
    elif order == 'cappuccino':
        return order

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
        orderChooser(order)
        print(f"Please insert coins.")
        drinkCost = MENU[order]["cost"]
        purchase()
    else:
        print(f"Please enter a valid option.")

    if order == 'report':
        report()


