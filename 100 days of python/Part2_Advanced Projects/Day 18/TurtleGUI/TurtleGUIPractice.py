from turtle import *
import random
colors = ["IndianRed", "DeepSkyBlue", "CornFlowerBlue", "LightSeaGreen", "wheat", "SeaGreen", "SlateGray"]
direction = ["right", "left"]
directionAngle = [1, 2, 3] #fix this

turtleObject = Turtle()
screen = Screen()
turtleObject.shape("turtle")
turtleObject.color("green")
turtleObject.pensize(7)
turtleObject.speed(3)

def randomWalk(object):
    #function to create a random walk pattern
    for i in range(100):
        object.forward(20)
        angle = 90*int(random.randint(directionAngle))
        if random.choice(direction) == "left":
            object.left(angle)
        else:
            object.right(angle)
        object.pencolor(random.choice(colors))


def drawDashedLine(object):
    for i in range(25):
       object.forward(5)
       object.penup()
       object.forward(5)
       object.pendown()

def drawShape(object):
    sides = 3
    while sides <= 11:
        for i in range(sides):
            object.forward(100)
            object.right(360/sides)
        sides+=1
        object.pencolor(random.choice(colors))

#drawShape(turtleObject)
randomWalk(turtleObject)
screen.exitonclick()