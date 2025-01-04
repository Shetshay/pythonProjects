from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        #self.write(f"Score ={self.score}", True, align="center")
        super().__init__()
        self.color("white")
        self.penup()
        self.score = 0
        self.goto(0, 280)
        self.hideturtle()
        #self.write(f"Score ={self.score}", move=False, align='center', font=('Arial', 8, 'normal'))
    def update_score(self):
        self.clear()
        self.write(f"Score = {self.score}", move=False, align='center', font=('Arial', 16, 'normal'))
        self.score += 1
