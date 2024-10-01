#Ankush Joshi
#Day 3/100
#Control Flow Project
print('''
    *******************************************************************************
              |                   |                  |                     |
     _________|________________.=""_;=.______________|_____________________|_______
    |                   |  ,-"_,=""     `"=.|                  |
    |___________________|__"=._o`"-._        `"=.______________|___________________
              |                `"=._o`"=._      _`"=._                     |
     _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
    |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
    |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
              |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
     _________|___________| ;`-.o`"=._; ." ` '`."/` . "-._ /_______________|_______
    |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
    /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
    /______/______/______/______/______/______/______/______/______/______/[TomekK]
    *******************************************************************************
''')

print("Welcome to Treasure Island. Your mission is to find the treasure.")
choice1 = input('You\'re at a cross road. Where do you want to go?\n          Type "left" or "right": ').lower()

if choice1 == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    choice2 = input('Type "wait" to wait for a boat or type "swim" to swim across the lake: ').lower()
    if choice2 == "wait":
        print("A boat has appeared! You get on board and it takes you to the island and find a cabin.")
        choice3 = input("The cabin has three doors: Red, Blue and Yellow, which one will you go into? ").lower()
        if choice3 == "yellow":
            print("You successfully found the treasure chest and left with your riches!")
        elif choice3 == "red":
            print("You opened the red door, and walked into the room only to find out that it was on fire.")
            print("Game Over")
        elif choice3 == "blue":
            print("You opened the blue door and got trapped inside with some wild beasts who ate you alive...")
            print("Game Over")
        else:
            print("You chose not to choose any of the doors and fell into a trap... Game over")
    elif choice2 == "swim":
        print("Oh no! You were attacked by a trout while swimming and died... Game Over")
elif choice1 == "right":
    print("Game over")

