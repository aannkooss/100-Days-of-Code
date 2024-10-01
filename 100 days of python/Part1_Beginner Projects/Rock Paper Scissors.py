#Ankush Joshi
#Day 4/100 - Randomisation and Python Lists
#Rock Paper Scissors
import random
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)           
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

userChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
computerChoice = random.randint(0,2)
#print(computerChoice)
choices = [rock, paper, scissors]
if userChoice == computerChoice:
    print("> You Chose:\n"+choices[userChoice])
    print("> Computer chose:")
    print(choices[computerChoice])
    print(">> It is a tie! <<")
elif userChoice == 0 and computerChoice == 1:
    print("> You Chose: \n"+choices[0])
    print("> Computer Chose:"+choices[1])
    print("Computer's paper beats your rock, you lose!")
elif userChoice == 0 and computerChoice == 2:
    print("> You Chose: \n"+choices[0])
    print("> Computer Chose: \n"+choices[2])
    print("Your rock crushes computer's scissors, you win!")
elif userChoice == 1 and computerChoice == 0:
    print("> You Chose:\n"+choices[1])
    print("> Computer Chose: \n"+choices[0])
    print("Your paper beats computer's rock, you win!")
elif userChoice == 1 and computerChoice == 2:
    print("> You Chose: \n"+choices[1])
    print("> Computer Chose: \n"+choices[2])
    print("Computer's scissor cuts your paper, you lose!")
elif userChoice == 2 and computerChoice == 0:
    print("> You Chose:\n"+choices[2])
    print(">Computer Chose:\n"+choices[0])
    print("Computer's rock crushes your scissors, you lose!")
elif userChoice == 2 and computerChoice == 1:
    print("> You Chose:\n"+choices[2])
    print("> Computer Chose:\n"+choices[1])
    print("Your scissors cut rock's paper, you win!")