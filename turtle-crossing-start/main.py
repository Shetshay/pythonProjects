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
cars = CarManager()

counter = 0

screen.listen()
screen.onkey(player.move, "w") # make sure not to include parenthesis on function call

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if counter % 80 == 0: # control how frequent we need to spawn cars
        cars.create_cars()
    cars.move_cars()
    #print(f"This is the PLAYER {player.distance(player)}")
    #print(f"This is the CAR{cars.distance(cars)}")
    #print(cars.cars[0].xcor())


    if cars.did_player_touch_car(player):
        score.game_over()
        game_is_on = False

    if int(player.ycor()) > 280:
        score.update_scoreboard()
        player.reset()
        cars.clear_cars()
    counter += 10

screen.exitonclick()
