from tkinter import *

def buttonClicked():
    newText = input.get()
    myLabel.config(text=newText)

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500,height=300)
window.config(padx=20, pady=20)

#Label
myLabel = Label(text="I am a label", font=("Arial", 24, "bold"))
myLabel["text"] = "New Text"
myLabel.config(text="New Text") #config will allow us to change more than just text, however like font and color
# myLabel.pack() #this displays the label to the screen - handles size and position
# myLabel.place(x=0,y=0) # more accurate way to place objects
myLabel.grid(row=0, column=0)

#Button
button = Button(text="Click Me", command=buttonClicked) # first param: button message. second param: function call
button.grid(row=2,column=2)

button2 = Button(text="New Button")
button2.grid(row=1, column=3)

#Input/Entry
input = Entry(width=10) # creating a text box entry object stored as input
input.grid(row=3,column=4)


window.mainloop() #this keeps the window open
