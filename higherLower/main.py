import random

from art import logo, vs
from game_data import data

counter = 0
score = 0
gameOver = False
used = []

def setup():
    global used
    global counter
    a = random.randint(0, len(data) - 1) # comparison A for 50
    b = random.randint(0, len(data) - 1) # comparison B for 50
    # TODO make for loop to check each used new comparison and change if match
    while a == b: # REROLL IF == to each other
        print(f"WE WERE == TO EACH OTHER")
        a = random.randint(0, len(data) - 1)  # comparison A for 50
        b = random.randint(0, len(data) - 1)  # comparison B for 50
        print(a, b)
    #print(f"This is {counter}")
    used.append(counter)
    used[counter] += a
    counter += 1
    print(f"This is {counter}")
    used.append(counter)
    used[counter] += b
    counter += 1
    print(f"This is {counter}")
    print(used)
    #print(len(data))
    for i in range(0,len(used)): # START AT 1 INSTEAD OF 0 BECAUSE THE FIRST RANDOM COMPARE DOESN'T NEED TO BE CHANGED
        #print(i)
        while a == used[i]:
            print(f'MATCH ONE: {a} was equal to {used[i]}')
            a = random.randint(0, len(data))
            #used[counter - 2] = a
            ## CHANGE TO data.[]?
            print(f'Now im: {a}')
            print(used)
        while b == used[i]:
            print(f'MATCH TWO: {b} was equal to {used[i]}')
            b = random.randint(0, len(data))
            #used[counter - 1] = b
            print(f'Now im: {b}')
            print(used)
    return data[a], data[b]

def game(a, b):
    global score
    global gameOver
    #print(logo)
    print(f"Compare A: {a["name"]}, a(n) {a["description"]}, from {a["country"]}.")
    print(f"their followers: {a["follower_count"]}")
    print(vs)
    print(f"Against B: {b["name"]}, a(n) {b["description"]}, from {b["country"]}.")
    print(f"their followers: {b["follower_count"]}")
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    if answer == 'a':
        if a["follower_count"] > b["follower_count"]:
            score += 1
            #print(logo)
            #print(f"You're right! Current score: {score}")
            return score, gameOver
    if answer == 'b':
        if b["follower_count"] > a["follower_count"]:
            score += 1
            #print(logo)
            #print(f"You're right! Current score: {score}")
            return score, gameOver
    else:
        print(logo)
        print(f"Sorry that's wrong. Final score: {score}")
        gameOver = True
        return score, gameOver

    #print(a["follower_count"])
    return score, gameOver



while not gameOver:
    print(logo)
    if score > 0:
        print(f"You're right! Current score: {score}")
    comparisonA, comparisonB = setup()
    highScore, gameOver = game(comparisonA, comparisonB)


