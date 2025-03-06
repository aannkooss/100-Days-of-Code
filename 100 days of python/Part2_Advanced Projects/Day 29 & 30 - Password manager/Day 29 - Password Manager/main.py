# Ankush Joshi
# February 26, 2025
# Day 29/100 - Password Manager
from encodings import search_function

# Importing Libraries
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# TO ADD: Add a verification mode to protect user security

def generatePassword():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
               'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
               'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
               'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Creating character arrays that pick random characters in each specified list
    passwordLetters = [choice(letters) for _ in range(randint(8, 10))]
    passwordSymbols = [choice(symbols) for _ in range(randint(2, 4))]
    passwordNumbers = [choice(numbers) for _ in range(randint(2, 4))]

    # Combines all arrays
    passwordList = passwordLetters + passwordSymbols + passwordNumbers
    shuffle(passwordList)

    password = "".join(passwordList)
    passwordInput.insert(0, f"{password}")

    # Copies password to clipboard for easy access
    pyperclip.copy(password)

def save():
    website = websiteInput.get()
    email = emailInput.get()
    password = passwordInput.get()
    newData = {website: {
        "Email": email,
        "Password": password
    }}

    # Case if website or password field are left empty
    if website == "" or password == "":
        messagebox.showerror(title="Error", message="You've left some fields blank. Please"
                                                          " fill them out before saving")
        return
    else:
        try: #executes this chunk first
            with open("data.json", "r") as dataFile:
                data = json.load(dataFile) # reads data
                data.update(newData)
        except FileNotFoundError: # if file is not found, create a new one
            with open("data.json", "w") as dataFile:
                json.dump(newData, dataFile, indent=4)
        else: # if it does work, then update the data
            data.update(newData)
            with open("data.json", "w") as dataFile:
                json.dump(data, dataFile, indent=4)
        finally: # clear inputs
            websiteInput.delete(0, END)
            passwordInput.delete(0, END)

# Search

def search():
    website = websiteInput.get()
    try:
        with open("data.json") as dataFile:
            data = json.load(dataFile)
    except FileNotFoundError:
        messagebox.showinfo(title="Error!", message="Data File doesnt exist!")
    else:
        if website in data:
            email = data[website]["Email"]
            password = data[website]["Password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showerror(title="Error!", message="Login details not found!")

# Creating window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Setting up canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo) #x,y must be half of height and width to center image
canvas.grid(row=0,column=1)

# Labels
websiteLabel = Label(text="Website:")
websiteLabel.grid(row=1,column=0)
websiteLabel.focus()
emailLabel = Label(text="Email/Username:")
emailLabel.grid(row=2,column=0)
passwordLabel = Label(text="Password:")
passwordLabel.grid(row=3,column=0)

# Inputs
websiteInput = Entry(width=18)
websiteInput.grid(row=1,column=1, columnspan=1)
emailInput = Entry(width=35)
emailInput.grid(row=2,column=1, columnspan=2)
emailInput.insert(0,  "joshiankush6@gmail.com")
passwordInput = Entry(width=18)
passwordInput.grid(row=3,column=1)

#Buttons
passwordButton = Button(text="Generate Password", command=generatePassword)
passwordButton.grid(row=3, column=2)
addButton = Button(text="add", command=save, width=33)
addButton.grid(row=4,column=1, columnspan=2)
searchButton = Button(text="Search", command=search, width=13)
searchButton.grid(row=1, column=2)

window.mainloop()