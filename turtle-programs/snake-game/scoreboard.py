from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')

class Score(Turtle):
    def __init__(self):
        #self.write(f"Score ={self.score}", True, align="center")
        super().__init__()
        self.color("white")
        self.penup()
        self.score = 0
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score = {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", move=False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.clear()
        self.update_scoreboard()
        self.score += 1
