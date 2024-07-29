import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbolCount = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbolValue = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def checkWinnings(columns, lines, bet, values):
    winnings = 0
    winningLines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbolToCheck = column[line]
            if symbol != symbolToCheck:
                break
        else:
            winnings += values[symbol]*bet
            winningLines.append(lines+1)

    return winnings, winningLines


def getSlotMachineSpin(rows, cols, symbols):
    allSymbols = []
    for symbol, symbolCount in symbols.items():
        for _ in range(symbolCount):
            allSymbols.append(symbol)

    columns = []
    for _ in range(cols): #runs the entire for loop as many times as there are columns
        column = [] #
        currentSymbols = allSymbols[:] #colon copies the second list into the first and treats the first as its own
        for _ in range(rows): #running this chunk for as many times as there are rows (predefined)
            value = random.choice(allSymbols) #value variable picks a random choice from the symbols list
            currentSymbols.remove(value) #this removes the value picked in the allSymbols list from the copied list
            column.append(value) #this adds the value into the column list

        columns.append(column) #this adds the "row" list to the column list

    return columns

def printSlotMachine(columns):
    for row in range(len(columns[0])): #creates the rows by getting the length of the amount of elements in columns,
                                       #columns are laid out like ___ but we want them to be like |
        for i, column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()



def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount

def getNumLines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES)+ ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Number must be between 1 and "+str(MAX_LINES))
        else:
            print("Please enter a number.")

    return lines

def getBet():
    while True:
        amount = input("What would you like to bet? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between {MIN_BET} - {MAX_BET}.")
        else:
            print("Please enter a number.")

    return amount

def spin(balance):
    lines = getNumLines()
    while True:
        bet = getBet()
        totalBet = bet * lines

        if totalBet > balance:
            print(f"You do not have enough to bet that amount, your current balance is ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to ${totalBet}")
    slots = getSlotMachineSpin(ROWS, COLS, symbolCount)
    printSlotMachine(slots)
    winnings, winningLines = checkWinnings(slots, lines, bet, symbolValue)
    print(f"You won ${winnings} on lines", *winningLines)
    #print(f"You won on lines", *winningLines)
    return winnings - totalBet

def main():
    balance = deposit()
    while True:
        print(f"> Current balance is: ${balance}")
        userChoice = input("\nPress enter to play. (q to quit) ")
        userChoice = userChoice.lower()
        if userChoice == "q":
            break
        balance += spin(balance)

    print(f"\n> You left with ${balance}")

main()