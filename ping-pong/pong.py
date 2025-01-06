from turtle import Screen, Turtle
from paddle import Paddle
import random
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)

game_is_on = True

r_player = Paddle()
l_player = Paddle()

screen.listen()
# screen.onkey(left_player.up, "w")
# screen.onkey(left_player.down, "s")
screen.onkey(r_player.up, "i")
screen.onkey(r_player.down, "k")


while game_is_on:
    screen.update()
    time.sleep(0.1)

    #rightPlayer.move()
screen.exitonclick()
