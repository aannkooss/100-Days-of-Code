# Ankush Joshi
# February 24, 2025
# Day 28/100 Pomodoro Timer

from tkinter import *
import math

#---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def resetTimer():
    window.after_cancel(timer)
    canvas.itemconfig(timerText, text="00:00")
    timerLabel.config(text="timer")
    check.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def startTimer():
    global reps
    reps += 1

    workSec = WORK_MIN * 60
    shortBreakSec = SHORT_BREAK_MIN * 60
    longBreakSec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countDown(longBreakSec)
        timerLabel.config(text="break", fg=RED)
    elif reps % 2 == 0:
        countDown(shortBreakSec)
        timerLabel.config(text="break", fg=PINK)

    else:
        countDown(workSec)
        timerLabel.config(text="work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countDown(count):

    countMin = math.floor(count / 60)
    countSec = count % 60
    if countSec < 10:
        countSec = f"0{countSec}"

    canvas.itemconfig(timerText, text=f"{countMin}:{countSec}")
    if(count > 0): # makes sure we dont go to negative
        global timer
        timer = window.after(1000, countDown, count-1)  # pass in time as ms

    else:
        startTimer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✔"
        check.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timerLabel = Label(text="timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
timerLabel.grid(row=1,column=2)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timerText = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2,column=2)

start = Button(text="start", command=startTimer, bg=YELLOW, highlightbackground=YELLOW)
start.grid(row=3,column=1)

reset = Button(text="reset", command=resetTimer, bg=YELLOW, highlightbackground=YELLOW)
reset.grid(row=3,column=3,)

check = Label(text="✔", fg=GREEN, bg=YELLOW, highlightbackground=YELLOW)
check.grid(row=4,column=2)


window.mainloop()
