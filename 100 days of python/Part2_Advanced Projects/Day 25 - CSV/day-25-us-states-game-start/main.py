import turtle
import pandas

# Screen setup
screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Load data
statesData = pandas.read_csv("50_states.csv")
statesArray = statesData["state"].to_list()
correctGuesses = []

# Main game loop
while len(correctGuesses) < 50:
    # Get user input inside the loop
    answerState = screen.textinput(title=f"{len(correctGuesses)}/50 States Correct",
                                   prompt="Please type a state name").title()

    # Check if guess is among 50 states
    if answerState == "Exit":
        # missingStates = []
        # for state in statesArray:
        #     if state not in correctGuesses:
        #         missingStates.append(state)

        # Shortening this code snippet using List Comprehension
        missingStates = [state for state in statesArray if state not in correctGuesses]

        newData = pandas.DataFrame(missingStates)
        newData.to_csv("StatesToLearn.csv")


        break
    if answerState in statesArray and answerState not in correctGuesses:
        correctGuesses.append(answerState)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        data = statesData[statesData["state"] == answerState]
        t.goto(x=int(data.x), y=int(data.y))
        t.write(answerState)