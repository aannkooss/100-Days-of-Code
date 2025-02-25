#Ankush Joshi
#Day 23 - Turtle Crossing Capstone Project
#November 22, 2024

#importing libraries/modules
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

#setting up screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

#setting up game objects
player = Player()
carManager = CarManager()
scoreboard = Scoreboard()

#setting up screen input
screen.listen()
screen.onkey(player.up, "w")
screen.onkey(player.down, "s")

game_is_on = True #command to control game flow
while game_is_on:
    time.sleep(0.1)
    screen.update()
    carManager.createCar()
    carManager.moveCars()

    #detects collision between turtle and cars
    for car in carManager.allCars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.gameOver()

    #detects if player is at finish line
    if player.isAtFinish():
        player.goToStart()
        carManager.levelUp()
        scoreboard.increaseLevel()

screen.exitonclick()