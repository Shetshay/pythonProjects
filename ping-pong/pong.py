from turtle import Screen, Turtle
from RightPlayer import RightPlayer
import random
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
#screen.tracer(0)

game_is_on = True

#rightPlayer = RightPlayer()
#leftPlayer = left_player()

pong = Turtle()

width = 20
height = 100

pong.speed("fastest")
pong.penup()
pong.shape("square")
pong.color("white")
pong.shapesize(stretch_wid=5,stretch_len=1)
pong.goto(350, 0)


screen.listen()

def up():
    new_y = pong.ycor() + 20
    pong.goto(pong.xcor(), new_y)

def down():
    new_y = pong.ycor() - 20
    pong.goto(pong.xcor(), new_y)
# screen.onkey(left_player.up, "w")
# screen.onkey(left_player.down, "s")
screen.onkey(up, "i")
screen.onkey(down, "k")


while game_is_on:
    screen.update()
    time.sleep(0.1)

    #rightPlayer.move()
screen.exitonclick()
