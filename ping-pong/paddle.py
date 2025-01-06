from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.pong = Turtle()
        self.pong.penup()
        self.pong.shape("square")
        self.pong.color("white")
        self.pong.shapesize(stretch_wid=5, stretch_len=1)
        self.pong.goto(350, 0)

    def up(self):
        new_y = self.pong.ycor() + 20
        self.pong.goto(self.pong.xcor(), new_y)

    def down(self):
        new_y = self.pong.ycor() - 20
        self.pong.goto(self.pong.xcor(), new_y)
