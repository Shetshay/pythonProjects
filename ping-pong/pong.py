from turtle import Screen, Turtle
import left_player, right_player
import random
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)

LEFT_PLAYER_STARTING_POSITION: (-280,0)
RIGHT_PLAYER_STARTING_POSITION: (280,0)

screen.listen()
screen.onkey(left_player.up, "w")
screen.onkey(left_player.down, "s")
screen.onkey(right_player.left, "i")
screen.onkey(right_player.right, "k")


MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

screen.exitonclick()
