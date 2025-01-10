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

screen.onkey(r_player.up, "i")
screen.onkey(r_player.down, "k")

screen.onkey(l_player.up, "w")
screen.onkey(l_player.down, "s")


while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # print(ball.distance(r_player.pong))
    if ball.distance(r_player) < 50 and ball.xcor() > 320 or ball.distance(l_player) < 50 and ball.xcor() < -320:
        print("Made contact")
        ball.bounce_x()
    # Detect R paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
    # Detect L paddle miss
    if ball.xcor() < -380:
        ball.reset_position()

        #ball.restart()



screen.exitonclick()
