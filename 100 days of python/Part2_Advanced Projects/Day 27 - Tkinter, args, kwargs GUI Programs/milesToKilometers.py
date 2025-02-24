# Ankush Joshi
# February 23, 2025
# Day 27/100 - Miles to Km converter

from tkinter import *

# Function to convert miles to km
def calculate():
    miles = float(input.get())
    kilometers = int(miles)*1.609
    print(kilometers)
    convertedText.config(text=f"{kilometers}")

# Initializing window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=250,height=150)

# Initializing screen objects and placing them using grid
input = Entry(width=8)
input.grid(row=1, column=2)

milesLabel = Label(text = "Miles")
milesLabel.grid(row=1,column=3)

equalLabel = Label(text = "is equal to ")
equalLabel.grid(row=2,column=1)

convertedText = Label(text="")
convertedText.grid(row=2,column=2)

kmLabel = Label(text="Km")
kmLabel.grid(row=2,column=3)

button = Button(text="Calculate", command=calculate) # Tying calculate function to button command
button.grid(row=3, column=2)

# Keeps screen open
window.mainloop()
