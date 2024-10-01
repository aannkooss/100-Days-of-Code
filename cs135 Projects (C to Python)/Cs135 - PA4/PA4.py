#Ankush Joshi
#June 24, 2024
#Cs135 PA4 - Python

def main():
    while True:
        print("\n--MENU--")
        print("(N)umbers\n(D)raw\nE(X)it\n")
        userChoice = input("Please Enter the character of your selection: ")

        if userChoice == 'n' or userChoice == 'N':
            number_counter()
        elif userChoice == 'd' or userChoice == 'D':
            draw_triangle()
        elif userChoice == 'x' or userChoice == 'X':
            print("Exiting Program...")
            exit()
        else:
            print("Invalid entry, please try again...")


def number_counter():
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


def draw_triangle():
    size = int(input("Please enter a size larger than 2: "))

    if size > 2:
        for row in range(1, size + 1):
            for space in range(size - row):
                print(" ", end="")
            for star in range((2 * row) - 1):
                print("*", end="")
            print()
    else:
        print("Size must be larger than 2.")


if __name__ == "__main__":
    main()