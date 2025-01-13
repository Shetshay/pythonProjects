from turtle import Turtle
from player import Player
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.cars = []
        self.create_cars()
        self.car_speed = 80

    def move_cars(self):
        for car in self.cars:
            car.forward(MOVE_INCREMENT)

    def create_cars(self):
        car = Turtle()
        car.color(random.choice(COLORS))
        car.penup()
        car.setheading(180)
        car.goto(295, random.randint(-280, 280))
        car.shape("square")
        car.shapesize(1, 3, 1)
        self.cars.append(car)

    def clear_cars(self):
        for car in self.cars:
            car.hideturtle() # we hide the turtle
        self.cars.clear() # we clear the car in the cars[] array


    def did_player_touch_car(self, player):
        for car in range(len(self.cars)):
            if player.distance(self.cars[car]) < 30:
                return True








