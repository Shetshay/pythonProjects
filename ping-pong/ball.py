from turtle import Turtle
from paddle import Paddle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_axis = 10
        self.y_axis = 10
        self.move_speed = 0.1

    def bounce_y(self):
        self.y_axis *= -1
    def bounce_x(self):
        self.x_axis *= -1
        self.move_speed *= 0.9

    def move(self):
        new_x = self.xcor() + self.x_axis
        new_y = self.ycor() + self.y_axis
        self.goto(new_x, new_y)

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()

