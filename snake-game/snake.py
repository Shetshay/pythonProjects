from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for starterBlocks in STARTING_POSITIONS:
            snake = Turtle()
            snake.shape("square")
            snake.color("white")
            snake.penup()
            snake.goto(starterBlocks)
            self.segments.append(snake)
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor() # 01 (second head)
            #print(new_x)
            new_y = self.segments[seg_num - 1].ycor() # 00 (third head/last head)
            self.segments[seg_num].goto(new_x, new_y) # set each head before 02 (head of snake) to follow
        self.segments[0].forward(20) # 02 (head)

    def up(self):
        self.segments[0].setheading(90)
        #self.segments[0].forward(20)
    def down(self):
        self.segments[0].setheading(270)
        #self.segments[0].forward(20)
    def left(self):
        self.segments[0].setheading(180)
        #self.segments[0].forward(20)
    def right(self):
        self.segments[0].setheading(0)
        #self.segments[0].forward(20)
