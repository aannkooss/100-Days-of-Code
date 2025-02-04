import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500,height=300)

#Label
myLabel = tkinter.Label(text="I am a label", font=("Arial", 24))
myLabel.pack() #this displays the label to the screen - handles size and position


window.mainloop() #this keeps the window open

#def add(n1, n2):
#   return n1+n2  #This limits the function to only taking the parameeters inside the function

#def add(*args):
# for n in args: #loops through arguments (stored in a tuple)
#   print(n)    #this allows for however many parameters