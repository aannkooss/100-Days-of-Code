#Ankush Joshi
#October 13, 2024
#Day 20/21 - Snake Game

# -------- THINGS TO TWEAK/ADD
# -------- add a menu so the user can choose to start
# -------- a pause functionality
# -------- store high score and display (scope will be within the game session)
# -------- some visual fixes
# -------- Try to figure out the input delay and if it can be fixed further
# -------- game modes -> hard (faster), expert (fastest or snake gets faster with every bite)
# -------- color settings for snake

# ---------------------------------------------------------------------------------------------------

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
#from helpers import Helpers

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")
def disableInput():
    screen.onkey(None, "Up")
    screen.onkey(None, "Down")
    screen.onkey(None, "Left")
    screen.onkey(None, "Right")

def game():
    snake.move()
    screen.update()

    if snake.head.distance(food) < 15: #'15' depends on food size
        food.newFood()
        score.increaseScore()
        snake.extend()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.gameOver()
            disableInput()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.gameOver()
        disableInput()
    else:
        screen.ontimer(game,100)

game()
screen.exitonclick()


# helpers = Helpers(screen)
#
# gameIsRunning = False
# highScore = 0


# #screen.onkey(snake.pause, "Space")
#
# def startGame():
#     global gameIsRunning
#     gameIsRunning = True
#     helpers.menu_turtle.clear()
#     screen.bgcolor("black")
#     gameLoop()
#
# def resetGame():
#     global gameIsRunning, highScore
#     gameIsRunning = True
#     snake.reset()
#     score.reset()
#     helpers.menu_turtle.clear()
#     gameLoop()
#
# def gameLoop():
#     global highScore
#
#     if gameIsRunning and not helpers.paused:
#         snake.move()
#         screen.update()
#
#         if snake.head.distance(food) < 15:
#             food.newFood()
#             score.increaseScore()
#             snake.extend()
#
#             for segment in snake.segments:
#                 if segment == snake.head:
#                     pass
#                 elif snake.head.distance(segment) < 10:
#                     highScore = helpers.highScore(score.score, highScore)
#                     helpers.gameOver(score.score, highScore)
#                     screen.onkey(resetGame, "space")
#                     return
#
#             if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor > 290 or snake.head.ycor < -290:
#                 highScore = helpers.highScore(score.score, highScore)
#                 helpers.gameOver(score.score, highScore)
#                 screen.onkey(resetGame, "space")
#                 return
#
#             screen.ontimer(gameLoop(), 100)
#
# helpers.startMenu()
# screen.listen()
# screen.onkey(startGame, "space")
#
# screen.onkey(lambda: helpers.pause(snake, food, score), "p")
#
# screen.exitonclick()

# -----------------------------------------------------------------------------





