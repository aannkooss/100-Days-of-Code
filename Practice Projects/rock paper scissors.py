import random

while True:
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("\nRock, paper or scissors? ").lower()

    if player == computer:
        print("\nplayer: ", player)
        print("computer: ", computer)
        print("Its a tie!")

    elif player == "rock":
        if computer == "paper":
            print("\nplayer: ", player)
            print("computer: ", computer)
            print("You Lose")

        elif computer == "scissors":
            print("\nplayer: ", player)
            print("computer: ", computer)
            print("You Win!")

    elif player == "scissors":
        if computer == "rock":
            print("\nplayer: ", player)
            print("computer: ", computer)
            print("You Lose!")
        elif computer == "paper":
            print("\nplayer: ", player)
            print("computer: ", computer)
            print("You Win!")

    elif player == "scissors":
        if computer == "paper":
            print("\nplayer: ", player)
            print("computer: ", computer)
            print("You Win!")
        if computer == "rock":
            print("\nplayer: ", player)
            print("computer: ", computer)
            print("You Lose!")

    playAgain = None
    playAgainChoices = ["Y", "N"]

    while playAgain not in playAgainChoices:
        playAgain = input("Would you like to keep playing? (Y/N) ").upper()

    if playAgain != "Y":
        print("Thank you for playing!")
        break
print("")
