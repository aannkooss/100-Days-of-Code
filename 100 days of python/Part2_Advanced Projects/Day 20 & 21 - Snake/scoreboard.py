#Ankush Joshi
#Scoreboard class handles everything  to do with establishing and changing the score

from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.updateScore()
        self.hideturtle()

    def updateScore(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def gameOver(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)

    def increaseScore(self):
        self.score+=1
        self.clear()
        self.updateScore()

