from turtle import *
import random

def generateRandomRGB():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    randomColor = (r,g,b)
    return randomColor

def spinograph(object):
    for i in range(100):
        object.circle(100)
        object.right(4)
        object.color(generateRandomRGB())
        object.pencolor(generateRandomRGB())

colormode(255)
turtleObject = Turtle()
turtleObject.shape("turtle")
#turtleObject.color(generateRandomRGB())
screen = Screen()
turtleObject.speed("fastest")

spinograph(turtleObject)
screen.exitonclick()