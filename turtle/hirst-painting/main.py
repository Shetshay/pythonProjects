import colorgram
import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()  #set turtle class = to tim
turtle.colormode(255)
tim.pensize(20) # size of dot
tim.speed(0) # fastest speed
tim.hideturtle()

colors = colorgram.extract('image.jpg', 30)

rgb = []
rgb_value = ()

for color in colors:
        rgb_value = (color.rgb.r, color.rgb.g, color.rgb.b)
        rgb.append(rgb_value) # get the rgb values of 30 colors

#print(rgb)
# from output rgb
color_list = [(232, 231, 228), (204, 155, 90), (116, 162, 196), (230, 243, 236), (159, 82, 50), (152, 63, 97), (63, 99, 146), (244, 228, 236), (167, 154, 50), (218, 229, 238), (60, 123, 86), (193, 133, 158), (127, 185, 161), (189, 90, 123), (131, 27, 47), (226, 203, 121), (200, 94, 71), (82, 156, 130), (78, 22, 54), (43, 53, 106), (143, 35, 29), (152, 210, 193), (95, 123, 175), (75, 154, 166), (35, 36, 78), (228, 166, 188), (25, 63, 42), (152, 209, 217), (82, 38, 29), (32, 84, 59)]

tim.setheading(225)
tim.penup()
tim.forward(300)
tim.setheading(0) # start at the bottom left of the screen instead of the middle so our hirst painting doesn't go OOB

for x in range(10): #ten rows
    for y in range(10): #ten columns
        #turtle.color(random.choice(color_list))
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.forward(50)
    tim.back(500) # start at the beginning
    tim.left(90)
    tim.forward(40)
    tim.right(90)
    tim.pendown()

screen = Screen()
screen.exitonclick() #close app on click
