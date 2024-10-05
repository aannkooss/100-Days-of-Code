import turtle as t
import random
colors = ["IndianRed", "DeepSkyBlue", "CornFlowerBlue", "LightSeaGreen", "wheat", "SeaGreen", "SlateGray"]
directionAngle = [1, 2, 3, 4]


def drawDashedLine(object):
    #function to draw a dashed line
    for i in range(25):
       object.forward(5)
       object.penup()
       object.forward(5)
       object.pendown()

def drawShape(object):
    #function to draw shapes - starting from a triangle and increasing in sides
    sides = 3
    while sides <= 11:
        for i in range(sides):
            object.forward(100)
            object.right(360/sides)
        sides+=1
        object.pencolor(random.choice(colors))

def randomWalk(object):
    #function to create a random walk pattern
    for i in range(200):
        heading = 90*random.choice(directionAngle)
        object.forward(30)
        object.setheading(heading)
        object.pencolor(generateRandomRGB())

def generateRandomRGB():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    randomColor = (r,g,b)

    return randomColor

t.colormode(255)
turtleObject = t.Turtle()
screen = t.Screen()
turtleObject.shape("turtle")
turtleColor = turtleObject.color(generateRandomRGB())
turtleObject.pensize(7)
turtleObject.speed(7)

randomWalk(turtleObject)
screen.exitonclick()