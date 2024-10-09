from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

def moveForward():
    turtle.forward(10)

screen.listen()
screen.onkey(key="w", fun=moveForward)
screen.exitonclick()