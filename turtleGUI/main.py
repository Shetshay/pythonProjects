from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("arrow")
#triangle
#square
#pentagon
#hexagon
#heptagon
#octagon
#nonagon
#decagon
# are the shapes we need to draw on the screen

# of sides / 360 degrees for angle
counter = 3 # start at triangle
while counter < 10: # end at decagon
    for _ in range (counter): # draw each shape, once done with current shape move to the next
        tim.forward(100) # draw forward
        tim.right(360/counter) # calculate angle to start rotating to correctly draw the shape
    counter += 1 # add 1 side to the shape we are drawing until we reach 10 (decagon)
    r = random.uniform(0.1, 1.0)
    g = random.uniform(0.1, 1.0)
    b = random.uniform(0.1, 1.0) # generate random colors
    colorChange = (r, g, b)
    tim.pencolor(colorChange) # change color

screen = Screen()
screen.exitonclick() #close app on click
