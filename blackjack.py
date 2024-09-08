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

def drawCardsForMe():
     #print(f"This is {counter}")
     my_cards[f"{counter}"] = random.choice(cards)
     computer_cards[f"{counter}"] = random.choice(cards)
     return my_cards[f"{counter}"]

def output(myDrawnCards, TOTAL, BOT_TOTAL):
    if TOTAL > 21:
        loopStatus = False
        return winner(TOTAL, BOT_TOTAL, loopStatus)
    elif TOTAL < 21 and counter > 0:
        print(counter)
        print(f"Your cards: [{myDrawnCards}], current score: ", end="")
    for adding in range(counter):
        #print(f"This is myTotal: {myTotal}")
        #print(f"{my_cards[f'{adding}']}")
        TOTAL = my_cards[f"{adding}"] + TOTAL
        BOT_TOTAL = computer_cards[f"{adding}"] + BOT_TOTAL
        if TOTAL > 21:
            loopStatus = False
            return winner(TOTAL, BOT_TOTAL, loopStatus)
        #print(f"{computer_cards['1']}")
        #botTotal += computer_cards[f"{adding}"]
        # if myTotal > 21:
        #     return winner(myTotal, botTotal)
        #print(f"This is my_cards adding: {my_cards[f"{adding}"]}")
    print(TOTAL)
    print(f"Computer's first card: {computer_cards['0']}")

    return TOTAL

def winner(myTotal, botTotal, endGame):
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
    #print(display)
    return endGame

def play_a_game(play):
    while play != 'y':
        play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        if play == 'y':
            return play
        elif play == 'n':
            return play

def LOGO(counter): # TODO MOVE THIS BACK DOWN IF ISSUES ARISE
    print(art.logo)
    computer_cards["0"] = random.choice(cards)
    for x in range(startingCounter):
        drawCardsForMe()
        counter += 1
    return drawCardsForMe(), counter

if (play_a_game(start)) == 'y':
    print("*********************")
    LOGO(counter)

    output(my_cards.values(), TOTAL, BOT_TOTAL)
    while display := input("Type 'y' to get another card, type 'n' to pass: ") != "n":
        #print(f"THIS IS DISPLAY IN MAIN WHILE LOOP: {display}")
        drawCardsForMe()
        counter += 1
        #output(my_cards.values(), TOTAL, BOT_TOTAL)

        if not output(my_cards.values(), TOTAL, BOT_TOTAL):
            counter = 0
            startingCounter = 2
            botCounter = 0
            play_a_game(start)
            my_cards = {}
            computer_cards = {}
            counter += LOGO(counter)

        else:
            print("\n\n ----------------------- \n\n")
            #output(my_cards.values(), TOTAL, BOT_TOTAL)
        #print(f"THIS IS DISPLAY: {display}")
        startingCounter = startingCounter + 1
        botCounter = botCounter + 1

    #winner calculation
    #winner()
