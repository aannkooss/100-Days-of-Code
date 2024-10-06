#Ankush Joshi
#October 6, 2024
#Day 18/100 - Hirst Painting

from turtle import *
import random
colormode(255)
colorList = [(238, 248, 243), (226, 237, 246), (30, 106, 145), (229, 153, 80), (15, 169, 207), (148, 79, 30), (6, 57, 97), (31, 134, 77), (214, 133, 162), (138, 32, 51), (205, 156, 22), (118, 172, 194), (213, 93, 124), (235, 211, 85), (6, 103, 66), (145, 185, 167), (216, 209, 11), (3, 69, 136), (15, 49, 43), (76, 83, 23), (243, 168, 151), (134, 59, 83), (53, 60, 15), (223, 170, 191), (230, 100, 40), (1, 90, 120), (71, 157, 105), (164, 29, 25), (165, 207, 191), (147, 210, 222), (97, 128, 164), (170, 192, 218), (81, 32, 74)]

#10x10 rows of spots
#20 in size, 50 in space

def drawPainting(turtleObject):
   #sets the pen up so we can move to bottom left
   turtleObject.penup()
   turtleObject.speed("fastest")

    #sets start position
   turtleObject.setheading(225)
   turtleObject.forward(300)
   turtleObject.setheading(0)

   for i in range(10):
        for j in range(10): #draws dot at a random color
            turtleObject.pendown()
            turtleObject.dot(20, random.choice(colorList))
            turtleObject.penup()
            turtleObject.forward(50)

        #moves to top of next row
        turtleObject.setheading(90)
        turtleObject.forward(50)
        turtleObject.setheading(180)
        turtleObject.forward(500)
        turtleObject.setheading(0)

pointer = Turtle()
screen = Screen()
pointer.hideturtle()
drawPainting(pointer)

screen.exitonclick()