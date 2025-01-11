from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        #time.sleep(0.5)
        self.hideturtle()
        self.penup()
        self.cars = []
        self.create_cars()

    def clear_cars(self):
        self.clear()

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






