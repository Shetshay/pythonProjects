from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

setup = 0

snake = Turtle()

for starterBlocks in range(0,3):
    starterBlocks = Turtle()
    starterBlocks.shape("square")
    starterBlocks.color("white")
    starterBlocks.goto(x=setup, y=0)
    setup -= 20


screen.exitonclick()