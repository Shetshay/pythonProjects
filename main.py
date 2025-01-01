import turtle

from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

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
        all_turtles.append(color)



# tim = Turtle(shape="turtle")
# tim.color(random.choice(colors))
# tim.penup()
# tim.goto(x=-230,y=-100)

create_turtle()

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            #print(f"{turtle.pencolor} has won!")
            if user_bet.lower() == turtle.pencolor.lower():
                print(f"Your guess was right! Congrats! 🥳{turtle.pencolor()} has won!")
            else:
                print(f"Oh no! Your guess was wrong :( {turtle.pencolor()} won, not {user_bet}!")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()

