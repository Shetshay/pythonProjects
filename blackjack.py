import random
import art

start = ''
myFinalScore = ''
TOTAL = 0
BOT_TOTAL = 0
startingCounter = 2
botCounter = 0
counter = 0
my_cards = {}
computer_cards = {}
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
display = ''

def starterCards():
     my_cards[f"{counter}"] = random.choice(cards)
     computer_cards[f"{counter}"] = random.choice(cards)
     return my_cards[f"{counter}"]

def updateMyCards(counter):
    my_cards[f"{counter}"] = random.choice(cards)
    return my_cards[f"{counter}"]

def updateBotCards(counter):
    computer_cards[f"{counter}"] = random.choice(cards)
    return computer_cards[f"{counter}"]

def myOutput(TOTAL):
    TOTAL = 0
    for adding in range(counter):
        TOTAL = my_cards[f"{adding}"] + TOTAL
        #print(f"wtf wtf wtf wtf wtf wtf wtf{TOTAL}")
    return TOTAL

def botOutput(BOT_TOTAL):
    BOT_TOTAL = 0
    for adding in range(counter):
        BOT_TOTAL = computer_cards[f"{adding}"] + BOT_TOTAL
    return BOT_TOTAL

def winner(myTotal, botTotal, endGame):
    print("THIS IS MY CARDS: ")
    print(my_cards)
    print("\n")
    print(f"Your final hand: [", end="")
    for keys in my_cards:
        print(f"{my_cards[f'{keys}']},", end="")
        #myFinalScore += my_cards[x]
    print(f"] final score: {myTotal}")
    #for addingMyScore in
    print("Computer's final hand: [", end="")
    for y in computer_cards:
        print(f"{computer_cards[f'{y}']},", end="")
    print(f"] final score: {botTotal}")
    if myTotal == botTotal:
        endGame = True
        print("Draw 🙃")
        return endGame
    if myTotal > 21:
        endGame = True
        print("You went over. You lose 😭")
        return endGame
    if myTotal < 21 and botTotal > 21:
        endGame = True
        print("Opponent went over. You win 😄")
        return endGame
    if myTotal < 21 and botTotal < 21:
        if myTotal > botTotal:
            print("You win 😃")
            endGame = True
            return endGame
        else:
            print("You lose 😤")
            endGame = True
            return endGame
    return endGame

def play_a_game(play):
    while play != 'y':
        play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        if play == 'y':
            LOGO()
            return play
        elif play == 'n':
            return play

def draw_a_card():
        draw = input("Type 'y' to get another card, type 'n' to pass: ")
        if draw == 'y':
            return draw
        elif draw == 'n':
            return draw
        else:
            draw = input("Please type 'y' to get another card, OR type 'n' to pass. ")
            return draw

def LOGO():
    print(art.logo)
    return

def output():
    print(my_cards)
    print("Your cards: [", end="")
    for adding in range(counter):
        print(my_cards[f'{adding}'], end=",")
    print(f"] current score: ", end="")
    print(TOTAL)
    print(f"Computer's first card: {computer_cards['0']}")

start = play_a_game(start)
while start != 'n':
    computer_cards["0"] = random.choice(cards)
    for x in range(startingCounter):
        starterCards()
        counter += 1
    if counter == 2:
        TOTAL = myOutput(TOTAL)
        BOT_TOTAL = botOutput(BOT_TOTAL)
    if TOTAL <= 21:
        output()
        display = draw_a_card()
    while display != "n":

        updateMyCards(counter)
        updateBotCards(counter)
        counter += 1

        TOTAL = myOutput(TOTAL)
        BOT_TOTAL = botOutput(BOT_TOTAL)
        if TOTAL <= 21:
            output()
            display = draw_a_card()
        #print(TOTAL)
        #print(BOT_TOTAL)
        if TOTAL > 21:
            counter = 0
            startingCounter = 2
            botCounter = 0
            my_cards = {}
            computer_cards = {"0": random.choice(cards)}
            for x in range(startingCounter):
                starterCards()
                counter += 1
            winner(myTotal = TOTAL, botTotal= BOT_TOTAL, endGame=True)
            start = ''
            TOTAL = 0
            BOT_TOTAL = 0
            play_a_game(start)

        if display == "n":
            print("I NEED TO TEST IF IT ENTERED THIS FUNCTION")
            winner(myTotal = TOTAL, botTotal= BOT_TOTAL, endGame=None)
            TOTAL = 0
            BOT_TOTAL = 0
            counter = 0
            startingCounter = 2
            botCounter = 0
            my_cards = {}
            computer_cards = {"0": random.choice(cards)}
            for x in range(startingCounter):
                starterCards()
                counter += 1
            break

    #startingCounter = startingCounter + 1
    #botCounter = botCounter + 1
    start = play_a_game(start)
    #break

print("Thank you for playing!")
