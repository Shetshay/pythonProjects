from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import random
import time

ball = Turtle()
ball.penup()

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)

game_is_on = True

r_player = Paddle(350, 0)
l_player = Paddle(-350, 0)

ball = Ball()

screen.listen()

screen.onkey(l_player.up, "w")
screen.onkey(l_player.down, "s")

screen.onkey(r_player.up, "i")
screen.onkey(r_player.down, "k")


while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

screen.exitonclick()
