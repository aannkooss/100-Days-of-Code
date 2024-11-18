from turtle import Screen, Turtle

screen = Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("Pong")
#screen.tracer(0)

paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(350,0)

def up(){

}

screen.listen()
screen.onkey(up,"Up")


screen.exitonclick()