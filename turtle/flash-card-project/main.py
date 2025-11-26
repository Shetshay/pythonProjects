from tkinter import *
import turtle
from turtle import Turtle, Screen
from tkinter import messagebox
import random

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50)

screen = turtle.Screen()
image = "images/card_front.png"
screen.addshape(image)
turtle.shape(image)

canvas = Canvas(width=800, height=526, highlightthickness=0)
canvas.grid(column=1 , row=0 )

button = Button(image=image, highlightthickness=0)


window.mainloop()