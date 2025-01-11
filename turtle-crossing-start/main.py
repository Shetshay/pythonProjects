import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Turtle Crossing")
screen.setup(width=600, height=600)
screen.tracer(0)

score = Scoreboard()
player = Player()

screen.listen()
screen.onkey(player.move, "w") # make sure not to include parenthesis on function call

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if player.ycor() > 280:
        score.update_scoreboard()
        player.reset()
