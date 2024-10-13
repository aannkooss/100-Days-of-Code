from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__() #inherits everything from turtle class
        self.shape("circle") #change this to a different shape later
        self.color("red")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5) #change this as well
        self.speed("fastest")

    def newFood(self):
        randomX = random.randint(-280,280)
        randomY = random.randint(-280,280)
        self.goto(randomX+0.5, randomY+0.5)