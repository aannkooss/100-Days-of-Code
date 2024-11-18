from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.xMove = 10
        self.yMove = 10
        self.moveSpeed = 0.08

    def move(self):
        newX = self.xcor() + self.xMove
        newY = self.ycor() + self.yMove
        self.goto(newX, newY)

    def yBounce(self):
        self.yMove *= -1 #inverts ball's y direction

    def xBounce(self):
        self.xMove *= -1
        self.moveSpeed *= 0.9

    def resetPosition(self):
        self.goto(0,0)
        self.moveSpeed = 0.08
        self.xBounce()