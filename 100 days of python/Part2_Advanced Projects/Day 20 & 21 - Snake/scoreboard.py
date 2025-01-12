#Ankush Joshi
#Scoreboard class handles everything  to do with establishing and changing the score

from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
class Scoreboard(Turtle):

    file = open("data.txt")
    score = file.read()
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.updateScore()
        self.hideturtle()

    def updateScore(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.updateScore()

    def increaseScore(self):
        self.score += 1
        self.clear()
        self.updateScore()

