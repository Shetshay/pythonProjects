from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

starting_positions = [(0,0), (-20, 0), (-40, 0)]

segments = []

for starterBlocks in starting_positions:
    snake = Turtle()
    snake.shape("square")
    snake.color("white")
    snake.penup()
    snake.goto(starterBlocks)
    segments.append(snake)

#screen.update()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor() # 01 (second head)
        new_y = segments[seg_num - 1].ycor() # 00 (third head/last head)
        segments[seg_num].goto(new_x, new_y) # set each head before 02 (head of snake) to follow
    segments[0].forward(20) # 02 (head)




screen.exitonclick()