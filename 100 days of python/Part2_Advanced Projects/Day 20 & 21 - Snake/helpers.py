# #Ankush Joshi
# #Helpers - this will contain all the functions for the extra functionality
#
# from turtle import Screen, Turtle
# class Helpers:
#     def __init__(self, screen):
#         self.screen = screen
#         self.paused = False
#         self.menu_turtle = Turtle(visible = False)
#         self.menu_turtle.color("white")
#         self.menu_turtle.penup()
#
#     def draw(self, message, x, y, font=("Arial", 24, "normal")):
#         self.menu_turtle.goto(x,y)
#         #self.menu_turtle.clear()
#         self.menu_turtle.write(message, align="center", font=font)
#
#     def startMenu(self):
#         self.screen.clear()
#         self.screen.bgcolor("black")
#         self.draw("Welcome to Snake!", 0, 50)
#         self.draw("Press 'space' to Start", 0,0)
#         self.draw("Press 'm' for the Menu", 0,-30)
#         self.draw("Press 'p' to pause", 0,-60)
#         self.draw("Press 'q' to quit", 0,-90)
#
#     def pause(self):
#         if not self.paused:
#             self.screen.onkey(None, "w")
#             self.screen.onkey(None, "a")
#             self.screen.onkey(None, "s")
#             self.screen.onkey(None, "d")
#             self.paused = True
#             self.draw_text("Game Paused. Press 'p' to resume", 0,0)
#         else:
#             self.screen.onkey(snake.up, "w")
#             self.screen.onkey(snake.down, "s")
#             self.screen.onkey(snake.left, "a")
#             self.screen.onkey(snake.right, "d")
#             self.menu_turtle.clear()
#             self.paused = False
#
#
#
#     def highScore(self, currentScore, highScore):
#         if currentScore > highScore:
#             return currentScore
#         return highScore
#
#     def gameOver(self, currentScore, highScore):
#         self.screen.clear()
#         self.draw_text(f"Game Over! Your score {currentScore}",0,50)
#         self.draw_text(f"High Score: {highScore}",0,20)
#         self.draw_text("Press 'space' to Play Again", 0,-30)
#         self.screen.update()
#
#     def gameMode(self):
#         pass
#
#     def colorSettings(self):
#         pass