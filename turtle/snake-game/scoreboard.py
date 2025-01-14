from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')


class Score(Turtle):
    def __init__(self):
        #self.write(f"Score ={self.score}", True, align="center")
        super().__init__()
        self.color("white")
        self.penup()
        self.score = -1
        with open("data.txt", mode="r") as file:
            self.contents = file.read()
        self.high_score = self.contents
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"Game Over", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > int(self.high_score):
            with open("data.txt", mode="w") as file:
                file.write(f"{self.score}")
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    def update_score(self):
        self.score += 1
        self.update_scoreboard()
