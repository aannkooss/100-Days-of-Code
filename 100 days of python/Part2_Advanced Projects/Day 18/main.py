#import turtle as t -> changes turtle to "t", so it makes it shorter to type (same as turtle)
from turtle import * #the * imports everything inside the module, instead of importing each on its own

# timmyTheTurtle = Turtle()
# timmyTheTurtle.shape("turtle")
# timmyTheTurtle.color("green")
# timmyTheTurtle.forward(180)
# timmyTheTurtle.right(90)

#Exercise 1 - Draw a square
tim = Turtle()
tim.shape("turtle")
tim.color("green")

for i in range(4):
    tim.forward(100)
    tim.right(90)

screen = Screen()
screen.exitonclick()
