#Ankush Joshi
#June 23, 2024
#Cs135 PA3 - Python

while True:
    print("\n--MENU--")
    print("(N)umbers\n(D)raw\nE(X)it\n")
    userChoice = input("Please Enter the character of your selection: ")

    if userChoice == "N" or userChoice == "n":
        while True:
            number = int(input("Please enter a number (0 to stop) "))

            if number != 0:
                count = 0
                i = number
                while i > 0:
                    i //= 10
                    count += 1
                print("Your number " + str(number) + " has " + str(count) + " digits")
            else:
                break

    if userChoice == 'D' or userChoice == 'd':
        size = int(input("Please enter a size larger than 2: "))

        if size > 2:
            for row in range(1, size+1):
                for space in range(size-row):
                    print(" ", end="")
                for star in range((2*row)-1):
                    print("*", end="")
                print()
        else:
            print("Size must be larger than 2.")

    if userChoice == 'x' or userChoice == 'X':
        print("Exiting Program...")
        exit()
