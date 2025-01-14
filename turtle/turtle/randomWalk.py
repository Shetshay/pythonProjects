import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
turtle.colormode(255)

tim.pensize(10)
tim.speed(6)
sides = [90, 180, 270, 360]

def changeColors():
    r = (random.randint(0, 255))
    g = (random.randint(0, 255))
    b = (random.randint(0, 255))
    rgb = (r, g, b)
    return rgb

for _ in range(50):
    tim.forward(30)
    tim.right(random.choice(sides))
    tim.color(changeColors())

screen = Screen()
screen.exitonclick() #close app on click
