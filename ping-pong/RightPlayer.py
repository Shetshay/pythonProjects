from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

RIGHT_PLAYER_STARTING_POSITION = (280,0)

class RightPlayer(Turtle):
    def __init__(self):
        super().__init__()
        self.segments = []
        self.shape("square")
        self.color("white")
        self.goto(RIGHT_PLAYER_STARTING_POSITION)

    def create_snake(self):
        for position in RIGHT_PLAYER_STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        snake = Turtle()
        snake.shape("square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.segments.append(snake)

    def up(self):
        if self.heading() != DOWN:
            self.setheading(UP)
        # self.segments[0].forward(20)

    def down(self):
        if self.heading() != UP:
            self.setheading(DOWN)
            # self.segments[0].forward(20)