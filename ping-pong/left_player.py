from turtle import Turtle

LEFT_PLAYER_STARTING_POSITION = (-280,0)

class LeftPlayer(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")