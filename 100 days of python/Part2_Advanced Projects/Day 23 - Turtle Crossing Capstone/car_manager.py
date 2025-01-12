from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.allCars = [] #creating an empty array where cars will be stored
        self.carSpeed = STARTING_MOVE_DISTANCE

    def createCar(self):
        randomChance = random.randint(1,6)
        if randomChance == 1: #spawns a car in 1/6 of the time
            newCar = Turtle("square")
            newCar.shapesize(stretch_wid=1, stretch_len=2) #making car a rectangular shape
            newCar.penup()
            newCar.color(random.choice(COLORS))
            randomY = random.randint(-250,250)
            newCar.goto(300, randomY) #cars will spawn at a random y coordinate
            self.allCars.append(newCar) #adding the car to the list of cars

    def moveCars(self):
        for car in self.allCars:
            car.backward(STARTING_MOVE_DISTANCE) #for every car in the array, it will move backwards (and just go off screen)

    def levelUp(self):
        self.carSpeed += MOVE_INCREMENT