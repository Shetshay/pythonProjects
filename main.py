from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

def create_turtle():
    distance = 100
    color_selection = 0
    for color in colors:
        color = Turtle(shape="turtle")
        color.penup()
        color.color((colors[color_selection]))
        color.goto(x=-230, y=-distance)
        distance -= 40
        color_selection += 1


# tim = Turtle(shape="turtle")
# tim.color(random.choice(colors))
# tim.penup()
# tim.goto(x=-230,y=-100)

create_turtle()

screen.exitonclick()

