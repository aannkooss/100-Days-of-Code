#Author: Ankush Joshi
#Date: August 9 2024
#Day 7/100 - Hangman game

#importing modules from other files or libraries
import random
from hangman_words import wordList
from hangman_art import stages
from hangman_art import logo
from hangman_art import lose
from hangman_art import win

#declaring variables to use later
lives = 6
gameOver = False

print(logo)
chosenWord = random.choice(wordList)

#creating empty lists to fill with letters/guesses later on
correctLetters = []
incorrectLetters = []

while not gameOver:
    userChoice = input("\nWould you like to play hangman (Y/N)? ").lower()
    if userChoice == "n":
        print("Exiting...")
        gameOver = True
    elif userChoice == "y":
        print("")
        while True:
            print(f"************************{lives}/6 LIVES LEFT************************")
            guess = input("Guess a letter: ").lower()

            if len(guess) > 1: #ensures that the user only inputs one letter and not multiple
                print("Please enter a single alphabetic character")
            else:
                if guess in correctLetters or guess in incorrectLetters: #checks if the letter has already been guessed
                    print(f"You've already guessed {guess}")
                    # noinspection PyUnboundLocalVariable
                    print(f"Word to guess: {display}")
                    continue

                display = ""
                for letter in chosenWord: #loops through chosenWord
                    if letter == guess: #if the letter in the word matches the guessed letter...
                        display += letter  #...add that letter to display
                        correctLetters.append(guess) #and add that letter to the list of correctLetters
                    elif letter in correctLetters:
                        display += letter #We will also add the letter to the display variable if it is correct
                    else:
                        display += "_"

                print(f"Word to guess: {display}") #prints the word with right letters filled in

                if guess not in chosenWord:
                    lives -= 1 #subtract lives by 1
                    incorrectLetters.append(guess) #add that guess to the list of incorrect letters
                    print(f"You guessed {guess}, that's not in the word. You lose a life (-1)")
                    if lives == 0: #game is over when lives are 0
                        gameOver = True
                        print("\n************************GAME OVER************************")
                        print(lose)
                        print(f"The word was: {chosenWord.upper()}")
                        print("")
                        break

                if "_" not in display: #if there are no more _ in the word, it is guesses
                    gameOver = True
                    print(f"\n>> Congratulations! You won with {lives} lives left!")
                    print(f">> The word was: {chosenWord.upper()}")
                    print(win)
                    break

                print(stages[lives]) #prints each stage of the hangman according to lives
                print(">> Incorrect Guesses:", " ".join(incorrectLetters)) #prints a list of incorrect guesses

    else:
        print(">> Please type Y or N <<")
