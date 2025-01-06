from turtle import Screen, Turtle
from RightPlayer import RightPlayer
import random
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)

game_is_on = True

rightPlayer = RightPlayer()
#leftPlayer = left_player()

screen.listen()
# screen.onkey(left_player.up, "w")
# screen.onkey(left_player.down, "s")
screen.onkey(rightPlayer.up, "i")
screen.onkey(rightPlayer.down, "k")


while game_is_on:
    screen.update()
    time.sleep(0.1)

    #rightPlayer.move()
screen.exitonclick()
