#Ankush Joshi
#July 1, 2024
#PA6 - Python
def main():
    tax = 0.0827
    filePath = 'sando.txt'
    RECEIPT = "receipt.txt"
    price = 0

    try:
        temp, size, chips, drinkSize, tip = read(filePath)
    except FileNotFoundError:
        print("Unable to open file")

    print(f"{temp} {size}\n{chips}\n{drinkSize}\n{tip}")

    try:
        write(RECEIPT, temp, chips, drinkSize, size, tip, price, tax)
    except Exception as e:
        print(f"Can't write to file")
        return


def read(filePath):
    with open(filePath, 'r') as file:
        lines = file.readlines()
    lines = [line.strip() for line in lines]

    temperature = lines[0][0]
    subSize = int(lines[0][2])
    chip = lines[1]
    drink = lines[2]
    tipAmount = int(lines[3])

    return temperature, subSize, chip, drink, tipAmount


def write(filePath, temp, chips, drinkSize, size, tip, price, tax):
    with open(filePath, 'w') as file:
        tipAmount = 0
        file.write("*****Your SANDWICH Order******\n")
        file.write(f"{size} inches")

        if temp == "H" or temp == "h":
            file.write(" HOT")
            price += 1.5
        else:
            file.write(" COLD")

        if size == 6:
            price += 6.99
        elif size == 12:
            price += 9.99

        file.write(f" sandwich: ${price:.2f}\n")

        if chips == "Y" or chips == "y":
            file.write("CHIPS:  $1.99\n")
            price += 1.99

        drinkPrice = 0
        if drinkSize == "S" or drinkSize == "s":
            file.write(f"SMALL Drink: $0.99\n")
            drinkPrice = 0.99
            price += 0.99
        elif drinkSize == "M" or drinkSize == "m":
            file.write(f"MEDIUM Drink: $1.99\n")
            drinkPrice = 1.99
            price += 1.99
        elif drinkSize == "L" or drinkSize == "l":
            file.write(f"LARGE Drink: $2.99\n")
            drinkPrice = 2.99
            price += 2.99

        file.write(f"______________________________\nSUBTOTAL: ${price:.2f}\n")

        tipAmount = price*tip/100
        price = price + price * tax + tipAmount
        file.write(f"plus {tax*100:.2f}% tax and {tip}% tip\n")
        file.write("==============================\n")
        file.write(f"The TOTAL is ${price:.2f}\n")


if __name__ == "__main__":
    main()

