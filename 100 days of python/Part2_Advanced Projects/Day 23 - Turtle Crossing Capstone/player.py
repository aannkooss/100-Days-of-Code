from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280 #y coordinate of finish line

class Player(Turtle):
    def __init__(self):
        super().__init__() #allows for Player to use all functions found in Turtle class
        self.shape("turtle")
        self.penup()
        self.goToStart()
        self.setheading(90) #sets direction that turtle is facing

    def isAtFinish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def goToStart(self):
        self.goto(STARTING_POSITION)

    def up(self):
        self.forward(MOVE_DISTANCE)

    def down(self):
        self.backward(MOVE_DISTANCE)
