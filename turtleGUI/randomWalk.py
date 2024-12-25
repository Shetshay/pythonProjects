from turtle import Turtle, Screen
import random

tim = Turtle()

tim.pensize(10)
tim.speed(6)
sides = [90, 180, 270, 360]
counter = 1

r = 0.2
g = 0.8
b = 0.5
rgb = (r, g, b)

def changeColors():
    global r
    global g
    global b
    global rgb
    r = (random.uniform(0.1, 1.0))
    g = (random.uniform(0.1, 1.0))
    b = (random.uniform(0.1, 1.0))
    rgb = (r, g, b)
    return

while counter < 50:
    tim.forward(30)
    tim.right(random.choice(sides))
    changeColors()
    tim.pencolor(rgb)
    counter += 1

screen = Screen()
screen.exitonclick() #close app on click
