import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

looper = 0
password = []

for x in letters:
   loop = random.randint(0, (len(letters) - 1))
   if looper < nr_letters:
        #print(letters[loop])
        password += letters[loop]
        #fullPassword[] = letters[loop]
        #print(password)
        #password[looper] = letters[loop]
        looper += 1
#print(password)

looper = 0
for x in symbols:
   loop = random.randint(0, (len(symbols) - 1))
   if looper < nr_symbols:
        #print(letters[loop])
        password += symbols[loop]
        looper += 1
#print(password)


looper = 0
for x in numbers:
   loop = random.randint(0, (len(numbers) - 1))
   if looper < nr_symbols:
        #print(letters[loop])
        password += numbers[loop]
        looper += 1
#print(password)

random.shuffle(password)

print("Your password is: ", end= "2")
for z in password:
    print(z, end="")

