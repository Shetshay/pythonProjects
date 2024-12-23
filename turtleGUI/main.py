from turtle import Turtle, Screen

tim = Turtle()
tim.shape("arrow")
#triangle
#square
#pentagon
#hexagon
#heptagon
#octagon
#nonagon
#decagon


for _ in range(15):
    tim.forward(10)
    tim.pu()
    tim.forward(10)
    tim.pd()


screen = Screen()
screen.exitonclick()
