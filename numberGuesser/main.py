import random
from art import logo

attempts = 10
randomNumber = random.randint(1, 100)
#print(randomNumber)

def start():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    return difficulty

def game(randomNumber):
    global attempts
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        answer = int(input("Make a guess: "))
        if answer < randomNumber:
            print("Too low.")
            print("Guess again.")
            attempts -= 1
        elif answer > randomNumber:
            print("Too high.")
            print("Guess again.")
            attempts -= 1
        if answer == randomNumber:
            print(f"You got it! The answer was {randomNumber}.")
            break
        if attempts <= 0:
            print("You've run out of guesses, you lose.")
            break

if start() == 'easy':
    game(randomNumber)
else:
    attempts -= 5
    game(randomNumber)

