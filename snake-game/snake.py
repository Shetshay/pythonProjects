from turtle import Turtle

class Snake:
    def __init__(self):
        self.segments = []
        self.starting_positions = [(0,0), (-20, 0), (-40, 0)]
        for starterBlocks in self.starting_positions:
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
