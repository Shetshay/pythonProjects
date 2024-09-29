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

def output(TOTAL, BOT_TOTAL):
    # if TOTAL > 21:
        # loopStatus = False
        # return winner(TOTAL, BOT_TOTAL, loopStatus)
    for adding in range(counter):
        TOTAL = my_cards[f"{adding}"] + TOTAL
        BOT_TOTAL = computer_cards[f"{adding}"] + BOT_TOTAL
        if TOTAL > 21:
            loopStatus = False
            return winner(TOTAL, BOT_TOTAL, loopStatus)
    if TOTAL <= 21:
        print("Your cards: [", end="")
        for adding in range(counter):
            print(my_cards[f'{adding}'], end=",")
        print(f"] current score: ", end="")
        print(TOTAL)
    print(f"Computer's first card: {computer_cards['0']}")
    #print(TOTAL)
    #print(BOT_TOTAL)
    return TOTAL, BOT_TOTAL

def draw():
    print("Draw 🙃")

def loseOver():
    print("You went over. You lose 😭")

def lose():
    print("You lose 😤")

def win():
    print("You win 😃")

def winOver():
    print("Opponent went over. You win 😄")

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
    if myTotal > 21:
        endGame = True
        loseOver()
    if myTotal < 21 and botTotal > 21:
        endGame = True
        winOver()
    if myTotal < 21 and botTotal < 21:
        if myTotal > botTotal:
            win()
            endGame = True
        else:
            lose()
            endGame = True

    if myTotal == botTotal:
        endGame = True
        draw()
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


start = play_a_game(start)

while start != 'n':
    computer_cards["0"] = random.choice(cards)
    for x in range(startingCounter):
        drawCardsForMe()
        counter += 1
    if counter == 2:
        TOTAL = output(TOTAL, BOT_TOTAL)
    display = draw_a_card()
    while display != "n":
        drawCardsForMe()
        counter += 1
        TOTAL, BOT_TOTAL = output(TOTAL, BOT_TOTAL)
        #if not TOTAL:
        display = draw_a_card()
        #print(TOTAL)
        #print(BOT_TOTAL)
        if TOTAL:
            print("IM OVERRR")
            counter = 0
            startingCounter = 2
            botCounter = 0
            my_cards = {}
            computer_cards = {}
            computer_cards = {"0": random.choice(cards)}
            for x in range(startingCounter):
                drawCardsForMe()
                counter += 1
            winner(myTotal = TOTAL, botTotal= BOT_TOTAL, endGame=True)
            start = ''
            play_a_game(start)
    if display == "n":
        winner(myTotal = TOTAL, botTotal= BOT_TOTAL, endGame=None)
        #TOTAL = 0
        #BOT_TOTAL = 0
        break
    startingCounter = startingCounter + 1
    botCounter = botCounter + 1
    start = play_a_game(start)
    #break

print("Thank you for playing!")
