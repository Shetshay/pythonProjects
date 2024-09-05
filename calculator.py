def add(n1, n2):
    print(f"{n1} + {n2} = {n1 + n2}")
    return n1 + n2

def subtract(n1, n2):
    print(f"{n1} - {n2} = {n1 - n2}")
    return n1 - n2

def multiply(n1, n2):
    print(f"{n1} * {n2} = {n1 * n2}")
    return n1 * n2

def divide(n1, n2):
    print(f"{n1} / {n2} = {n1 / n2}")
    return n1 / n2

def proceed(result):
    resume = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
    if resume == 'n':
        return
    elif resume == 'y':
        return operation(result)

def operation(result):
    global firstNumber
    print("+")
    print("-")
    print("*")
    print("/")
    chosen = input("Pick an operation: ")
    if result != "":
        firstNumber = result
    secondNumber = input("What's the next number?: ")
    if chosen == "+":
        proceed((add(float(firstNumber), float(secondNumber))))
    elif chosen == "-":
        proceed((subtract(float(firstNumber), float(secondNumber))))
    elif chosen == "*":
        proceed((multiply(float(firstNumber), float(secondNumber))))
    elif chosen == "/":
        proceed((divide(float(firstNumber), float(secondNumber))))

firstNumber = input("What's the first number?: ")
operation(firstNumber)
