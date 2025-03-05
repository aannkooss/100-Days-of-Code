# Ankush Joshi
# Flashcard Capstone Project
# March 5, 2025

from tkinter import *
import random
import pandas
import math

BACKGROUND_COLOR = "#B1DDC6"
currentCard = {}
wordsToLearn = {}
try: # First, try to open csv file
    # Reading data from file and storing it into a dictionary
    data = pandas.read_csv("data/WordsToLearn.csv")
except FileNotFoundError: # IF the file is not found, read from French words and create a new file
    originalData = pandas.read_csv("data/french_words.csv")
    wordsToLearn = originalData.to_dict(orient="records")
else: # Executes if first file IS found
    wordsToLearn = data.to_dict(orient="records") # orient keyword formats it properly into a dict

# Function to show next card
def nextCard():
    global currentCard, flipTimer
    window.after_cancel(flipTimer) # resets timer so that cards flip every time a new card is chosen
    currentCard = random.choice(wordsToLearn)
    canvas.itemconfig(cardTitle, text="French", fill="black")
    canvas.itemconfig(cardWord, text=currentCard["French"], fill="black")
    canvas.itemconfig(cardSide, image=frontFlashcard)
    flipTimer = window.after(3000, changeCard)

def nextCardCorrect():
    wordsToLearn.remove(currentCard)
    data = pandas.DataFrame(wordsToLearn)
    data.to_csv("data/WordsToLearn.csv", index=False) # index = False excludes numbers (indices)
    nextCard()

def changeCard():
    canvas.itemconfig(cardSide, image=backFlashcard)
    canvas.itemconfig(cardTitle, text="English", fill="white")
    canvas.itemconfig(cardWord, text=currentCard["English"], fill="white")

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flipTimer = window.after(3000, changeCard)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)

frontFlashcard = PhotoImage(file="images/card_front.png")
backFlashcard = PhotoImage(file="images/card_back.png")

cardSide = canvas.create_image(400, 263, image=frontFlashcard)
cardTitle = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
cardWord = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0,column=0, columnspan=2)

wrongImage = PhotoImage(file="images/wrong.png")
wrongButton = Button(image=wrongImage, command=nextCard, highlightthickness=0)
wrongButton.grid(row=1, column=0)

correctImage = PhotoImage(file="images/right.png")
correctButton = Button(image=correctImage,command=nextCardCorrect, highlightthickness=0)
correctButton.grid(row=1,column=1)

nextCard()

window.mainloop()
