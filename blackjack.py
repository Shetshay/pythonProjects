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
     my_cards[f"{counter}"] = random.choice(cards)
     computer_cards[f"{counter}"] = random.choice(cards)
     return my_cards[f"{counter}"]

def output(myDrawnCards, TOTAL, BOT_TOTAL):
    if TOTAL > 21:
        loopStatus = False
        return winner(TOTAL, BOT_TOTAL, loopStatus)
    for adding in range(counter):
        if TOTAL > 21:
            loopStatus = False
            return winner(TOTAL, BOT_TOTAL, loopStatus)
        TOTAL = my_cards[f"{adding}"] + TOTAL
        BOT_TOTAL = computer_cards[f"{adding}"] + BOT_TOTAL
        if TOTAL > 21:
            loopStatus = False
            return winner(TOTAL, BOT_TOTAL, loopStatus)
    if TOTAL <= 21:
        print(f"Your cards: [{myDrawnCards}], current score: ", end="")
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
            LOGO()
            return play
        elif play == 'n':
            return play

def LOGO():
    print(art.logo)
    return
start = play_a_game(start)

if start == 'y':
    #print("*********************")
    computer_cards["0"] = random.choice(cards)
    for x in range(startingCounter):
        drawCardsForMe()
        counter += 1
if start == 'n':
    print("asdifhsadilfshfaskfldfhjalfkas4308f4u3908fju349f4384hf)")
else:
    output(my_cards.values(), TOTAL, BOT_TOTAL)
    while display := input("Type 'y' to get another card, type 'n' to pass: ") != "n":
        if start == 'n':
            print("output(my_cards.values(), TOTAL, BOT_TOTAL)")
        #print(f"THIS IS DISPLAY IN MAIN WHILE LOOP: {display}")
        drawCardsForMe()
        counter += 1
        #output(my_cards.values(), TOTAL, BOT_TOTAL)

        if not output(my_cards.values(), TOTAL, BOT_TOTAL):

            counter = 0
            startingCounter = 2
            botCounter = 0
            my_cards = {}
            computer_cards = {}
            start = play_a_game(start)

            computer_cards["0"] = random.choice(cards)
            for x in range(startingCounter):
                drawCardsForMe()
                counter += 1
            output(my_cards.values(), TOTAL, BOT_TOTAL)
        startingCounter = startingCounter + 1
        botCounter = botCounter + 1
