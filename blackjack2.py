import random
# def drawCards():
#
from itertools import repeat
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def randomization():
    randomNumber = random.randint(0, len(cards) - 1)
    randomCard = cards[randomNumber]
    return randomCard

def startingCardsForMe(drawRepeat, myCards):
    for x in range(drawRepeat):
        myCards[f"{x}"] = randomization()
    return myCards

def startingCardsForBot(drawRepeat, botCards):
    for y in range(drawRepeat):
        botCards[f"{y}"] = randomization()
    return botCards
#
# def hit():

def outerLoop():
    outside_loop = input(f"Would you like to play Blackjack? 'y' or 'n'")
    return outside_loop

def innerLoop():
    inner_loop = input(f"Would you like to add a card? 'y' or 'n'")
    return inner_loop

def myArray(myCards):
    
def botArray(botCards):
    for x in botCards.keys():
        print(f"[")
#def showWinner():

    #startingCards()

my_cards = {}
bot_cards = {}
myArray = []
botArray = []

bigBrother = outerLoop()
littleBrother = innerLoop()

while bigBrother == 'y':
    startingCardsForMe(drawRepeat = 2, myCards= my_cards)
    startingCardsForBot(drawRepeat = 2, botCards = bot_cards)
    botArray(myArray, bot_cards)
    print(my_cards, bot_cards)
    if littleBrother == 'n':
        #showWinner()
        # Reset?
        print("")
    while littleBrother == 'y':
        innerLoop()
    outerLoop()


