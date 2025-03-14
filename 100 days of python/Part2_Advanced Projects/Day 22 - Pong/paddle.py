from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def up(self):
        changeInY = self.ycor() + 45
        self.goto(self.xcor(), changeInY)

    def down(self):
        changeInY = self.ycor() - 45
        self.goto(self.xcor(), changeInY)