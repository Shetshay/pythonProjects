from idlelib.configdialog import font_sample_text
from os import write
from car_manager import CarManager
from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 0
        self.goto(0, 260)
        self.game_speed = 0.1
        self.update_scoreboard()



    def update_scoreboard(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align="left", font=FONT)
        self.game_speed *= 0.9

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"Game Over", align="center", font=FONT)
        self.goto(0,-60)
        self.write(f"Level Highscore: {self.level}", align="center", font=FONT)

