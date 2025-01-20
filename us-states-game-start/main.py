import turtle
from os import write
from turtle import Turtle, Screen
import pandas
from score import Score

ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')

screen = turtle.Screen()
screen.setup(width=725, height=491) # width and height of image
screen.title("U.S. States Game")
image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

score = Score()

data = pandas.read_csv("50_states.csv")

amount_of_states = len(data.state)
end_game = False

already_guessed = []

state = Turtle()
state.penup()
state.speed("fastest")
state.shape("circle")
state.shapesize(0.2)

missed_states = []

while not end_game:
    answer_state = screen.textinput(title=f"{score.score}/{amount_of_states}", prompt="What's another state's name?")
    if answer_state == 'exit':
        end_game = True
        for state in range(amount_of_states):
            if data.state[state].upper() not in already_guessed:
                missed_states.append(data.state[state])

        states_game_score = {
            "Missed States": missed_states
            #"Count": squirrel_color_count
        }
        df = pandas.DataFrame(states_game_score)
        df.index += 1 # start series list at 1 instead of 0
        df.to_csv("states_game_score.csv")  # create new data
        print(df) # print data frame

    for guess in range(amount_of_states): # loop through the 50 states
        if data.state[guess].upper() == answer_state.upper() and already_guessed: # if the state in the data is what
            # they guessed and is in the already_guessed list
            print("You already guessed that!")
        if data.state[guess].upper() == answer_state.upper() and answer_state.upper() != already_guessed:
            # add .upper to make sure whichever caps user uses gets passed through
            # if the state is equal to the answer state and the answer state is not already in the already guessed list
            if answer_state.upper() not in already_guessed: # if statement that checks if it is a new state
                # once inside this if statement we know that the state that was guessed is NOT in the already_guessed
                # list, meaning it is a NEW guess, do all the appending and adding of score here
                already_guessed.append(answer_state.upper()) # add the state in all uppercase for easier comparison
                score.update_score()
                state.goto(data.x[guess], data.y[guess]) # go to its x and y coordinate from the csv
                state.write(answer_state)
            #print(already_guessed)
    if score.score >= amount_of_states:
        state.hideturtle()
        state.goto(0,0)
        state.write("Congratulations, you won!", align = ALIGNMENT, font = FONT)
        end_game = True

screen.exitonclick()