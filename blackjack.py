import random
import art

play = ''
myFinalScore = ''
startingCounter = 2
botCounter = 0
counter = 0
my_cards = {}
computer_cards = {}
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

# def loop(howManyLoops):
#     return outputCards(howManyLoops)

#  def outputCards(viewCards):
# #     #print(f"{my_cards["1"]}")
# #     #print(x)
# #     #print(f"{my_cards["1"]}")
# #     #print(f"{my_cards[f"{x}"]}")
#       return f"{my_cards[f"{viewCards}"]}"

def drawCardsForMe():
     #print(f"This is {counter}")
     my_cards[f"{counter}"] = random.choice(cards)
     computer_cards[f"{counter}"] = random.choice(cards)
     return my_cards[f"{counter}"] # TODO ADD COUNTER FOR COMPUTER CARDS

def output(myDrawnCards, botDrawnCards):
    myTotal = 0
    botTotal = 0
    print(f"Your cards: [{myDrawnCards}], current score: ", end="")
    for adding in range(counter):
        #print(f"This is myTotal: {myTotal}")
        #print(f"{my_cards[f'{adding}']}")
        myTotal = my_cards[f"{adding}"] + myTotal
        #print(f"{computer_cards['1']}")
        #botTotal += computer_cards[f"{adding}"]
        # if myTotal > 21:
        #     return winner(myTotal, botTotal)
        #print(f"This is my_cards adding: {my_cards[f"{adding}"]}")
    print(myTotal)
    print(f"Computer's first card: {computer_cards['0']}")
    return myTotal

def winner(myTotal, botTotal):
    print(f"Your final hand: [", end="")
    for keys in my_cards:
        print(f"{my_cards[f'{keys}']},", end="")
        #myFinalScore += my_cards[x]
    print(f"] final score: {myTotal}") # TODO INSERT FINAL SCORE HERE
    #for addingMyScore in
    print("Computer's final hand: [", end="")
    for y in computer_cards:
        print(f"{computer_cards[f'{y}']},", end="")
    print(f"] final score: {botTotal}") # TODO INSERT FINAL SCORE HERE

while play != 'y':
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n'")
    if play == 'n':
        break
if play == 'y':
    print(art.logo)
    # my_cards["1"] = random.choice(cards)
    # my_cards["2"] = random.choice(cards)
    computer_cards["0"] = random.choice(cards)
    for x in range(startingCounter):
        #print(x)
        drawCardsForMe()
        counter += 1
        #print(counter)
    output(my_cards.values(), computer_cards.values())
while display := input("Type 'y' to get another card, type 'n' to pass: ") != "n":
    #print(f"Your cards: [{loop(startingCounter)}], current score: {my_cards["1"] + my_cards["2"]}")
    #print(f"Computer's first card: {computer_cards["1"]}")
    #print(my_cards)

    #counter += 1
    #print(counter)

    drawCardsForMe()
    #print(counter)
    counter += 1
    #print(counter)
    output(my_cards.values(), computer_cards.values())
    # if myTotal > 21:
    #     print("You lose!")
    startingCounter = startingCounter + 1
    botCounter = botCounter + 1

#winner calculation
#winner()
