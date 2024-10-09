#Ankush Joshi
#October 9, 2024
#Day 19 - Etch a Sketch -> event listeners practice
from turtle import Turtle, Screen

pointer = Turtle()
screen = Screen()

def forward():
    pointer.forward(10)

def backward():
    pointer.backward(10)

def right():
    pointer.left(10)

def left():
    pointer.right(10)

def clear():
    pointer.reset()

screen.listen()

screen.onkey(key="w", fun=forward)
screen.onkey(key="s", fun=backward)
screen.onkey(key="a", fun=right)
screen.onkey(key="d", fun=left)
screen.onkey(key="c", fun=clear)

screen.exitonclick()