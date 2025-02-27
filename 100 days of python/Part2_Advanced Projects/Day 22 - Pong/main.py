from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

#THINGS TO ADD/COME BACK TO
# Winner/Loser system + play again
# Pause functionality

screen = Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

leftPaddle = Paddle((-350,0))
rightPaddle = Paddle((350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(rightPaddle.up,"Up")
screen.onkey(rightPaddle.down,"Down")
screen.onkey(leftPaddle.up,"w")
screen.onkey(leftPaddle.down,"s")

gameIsOn = True

while gameIsOn:
    time.sleep(ball.moveSpeed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.yBounce()

    if ball.distance(rightPaddle) < 50 and ball.xcor() > 320 or ball.distance(leftPaddle) < 50 and ball.xcor() < -320:
        ball.xBounce()

    if ball.xcor() > 380: #Passes right paddle
        ball.resetPosition()
        scoreboard.leftPoint()

    if ball.xcor() < -380: #Passes left paddle
        ball.resetPosition()
        scoreboard.rightPoint()
