#Ankush Joshi
#October 9, 2024
#Day 19 - Turtle Race
import random
from turtle import *

raceOn = False
screen = Screen()
screen.setup(500, 400) #500x400 (w by h) size
choices = ["indian red", "orange", "pink", "dark green", "blue", "purple"]
userChoice = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: "
                                                            "(Indian Red, Orange, Pink, Dark Green, Blue, Purple)")
while userChoice not in choices:
    userChoice = screen.textinput(title="Make your bet", prompt="Please type it as you see it (Indian Red, Orange, "
                                                                "Pink, Dark Green, Blue, Purple)").lower()
turtles = []
for color in choices:
    turtle = Turtle()
    turtle.color(color)
    turtles.append(turtle)

def createTurtle():
    for turtle in turtles:
        turtle.shape("turtle")

def positionTurtles():
    createTurtle()
    positionFactor = 50
    yValue = -150

    for turtle in turtles: #for loop to position turtles
        turtle.penup()
        yValue += positionFactor
        turtle.goto(-230, yValue)
        turtle.setheading(0)

if userChoice:
    raceOn = True

positionTurtles()

while raceOn:
    for turtle in turtles:
        if turtle.xcor() > 230:
            raceOn = False
            winner = turtle.pencolor()
            if winner == userChoice:
                print(f"You win! The {winner} turtle is the winner!")
            else:
                print(f"You lost! The {winner} turtle is the winner")

        randomDistance = random.randint(0,10)
        turtle.forward(randomDistance)

screen.exitonclick()