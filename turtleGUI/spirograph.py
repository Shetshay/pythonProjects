import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
turtle.colormode(255)
setAngle = 0


def randomColor():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    rgb = r, g, b
    return rgb

tim.speed(0)

turtle.color(randomColor())

while setAngle > -364:
    tim.color(randomColor())
    tim.circle(80)
    tim.seth(setAngle)
    setAngle -= 4


#tim.circle(50)



screen = Screen()
screen.exitonclick() #close app on click
