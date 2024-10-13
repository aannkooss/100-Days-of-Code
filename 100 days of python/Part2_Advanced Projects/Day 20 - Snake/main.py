#Ankush Joshi
#October 13, 2024
#Day 20/21 - Snake Game

# --------THINGS TO TWEAK
# -------- add a menu so the user can choose to start
# -------- a pause functionality
# -------- store high score and display (scope will be within the game session)
# -------- some visual fixes
# -------- Try to figure out the input delay and if it can be fixed further
# -------- game modes -> hard (faster), expert (fastest or snake gets faster with every bite)
# -------- color settings for snake

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

def game():
    snake.move()
    screen.update()

    if snake.head.distance(food) < 15: #'15' depends on food size
        food.newFood()
        score.increaseScore()
        snake.extend()

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            score.gameOver()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.gameOver()
    else:
        screen.ontimer(game,100)

game()
screen.exitonclick()