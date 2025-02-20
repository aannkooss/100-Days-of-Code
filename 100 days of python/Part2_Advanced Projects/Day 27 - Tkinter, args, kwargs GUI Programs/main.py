from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500,height=300)

#Label
myLabel = Label(text="I am a label", font=("Arial", 24, "bold"))
myLabel.pack(side="left") #this displays the label to the screen - handles size and position

myLabel["text"] = "New Text"
myLabel.config(text="New Text")


def buttonClicked():
    print("I got clicked")

button = Button(text="Click Me", command=buttonClicked )
button.pack()

window.mainloop() #this keeps the window open
