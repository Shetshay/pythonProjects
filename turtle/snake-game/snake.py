from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        snake = Turtle()
        snake.shape("square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.segments.append(snake)

    def extend(self):
        self.add_segment(self.segments[-1].position())


    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor() # 01 (second head)
            #print(new_x)
            new_y = self.segments[seg_num - 1].ycor() # 00 (third head/last head)
            self.segments[seg_num].goto(new_x, new_y) # set each head before 02 (head of snake) to follow
        self.segments[0].forward(20) # 02 (head)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        #self.segments[0].forward(20)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            #self.segments[0].forward(20)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            #self.segments[0].forward(20)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            #self.segments[0].forward(20)

