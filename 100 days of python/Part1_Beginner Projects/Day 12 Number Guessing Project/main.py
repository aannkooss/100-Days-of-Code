#Ankush Joshi
#August 17, 2024
#12/100 - Guessing number Game
import random
from art import logo

EASYLEVEL = 10
HARDLEVEL = 5

def checkAnswer(guess, number, attempts):
    if guess > number:
        print("Too high")
        return attempts - 1
    elif guess < number:
        print("Too low")
        return attempts - 1
    else:
        print(f"You got it! The answer was {number}")

def difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        return EASYLEVEL
    else:
        return HARDLEVEL

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    number = random.randint(1,100)
    attempts = difficulty()

    guess = 0
    while guess != number:
        print(f"You have - {attempts} - attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        attempts = checkAnswer(guess, number, attempts)

        if attempts == 0:
            print("You've run out of attempts, you lose!")
        elif guess != number:
            print("Guess again")

game()