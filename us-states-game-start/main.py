import turtle
from os import write
from turtle import Turtle, Screen
import pandas
from score import Score

ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')

screen = turtle.Screen()
screen.setup(width=725, height=491)
screen.title("U.S. States Game")
image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

score = Score()

data = pandas.read_csv("50_states.csv")

amount_of_states = len(data.state)
end_game = False

state = Turtle()
state.penup()
state.speed("fastest")
state.shape("circle")
state.shapesize(0.2)

while not end_game:
    answer_state = screen.textinput(title=f"{score.score}/{amount_of_states}", prompt="What's another state's name?")
    for guess in range(amount_of_states):
        if data.state[guess].upper() == answer_state.upper():
            score.update_score()
            state.goto(data.x[guess], data.y[guess])
            state.write(answer_state)
    if score.score >= amount_of_states:
        state.hideturtle()
        state.goto(0,0)
        state.write("Congratulations, you won!", align = ALIGNMENT, font = FONT)
        end_game = True

screen.exitonclick()