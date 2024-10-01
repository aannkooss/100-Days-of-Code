#Ankush Joshi
#June 25, 2024
#Cs135 PA5 - Python

def main():
    while True:
        userChoice = menuChoice()
        if userChoice == "X" or userChoice == 'x':
            print("Exiting calculator...")
            exit()

        real1, imaginary1 = complexNumberInput()
        real2, imaginary2 = complexNumberInput()

        match userChoice:
            case "A" | "a":
                realSum, imaginarySum = addition(real1, real2, imaginary1, imaginary2)
                print(f"\nThe Sum is: {realSum} + {imaginarySum}i")
                #break
            case "s" | "s":
                realDiff, imaginaryDiff = subtraction(real1, real2, imaginary1, imaginary2)
                print(f"\nThe difference is: {realDiff} - {imaginaryDiff}i")
                #break
            case "M" | "m":
                realProduct, imaginaryProduct = multiply(real1, real2, imaginary1, imaginary2)
                print(f"\nThe product is: {realProduct} * {imaginaryProduct}i")
                #break
            case "D" | "D":
                realQuotient, imaginaryQuotient = divide(real1, real2, imaginary1, imaginary2)
                print(f"\nThe quotient is: {realQuotient} / {imaginaryQuotient}i")
                #break
            case _:
                print("\nInvalid operation, please try again...")


def menuChoice():
    validChoices = {"A", "a", "S", "s", "M", "m", "D", "d", "X", "x"}
    while True:
        print("\nCOMPLEX NUMBER CALCULATOR")
        print("(A)dd\n(S)ubtract\n(M)ultiply\n(D)ivide\ne(X)it")
        userChoice = input("Enter the character of the operation you would like to do: ")
        if userChoice in validChoices:
            return userChoice
        else:
            print("Invalid choice, please select a valid character")


def complexNumberInput():
    realNumber = float(input("Enter the real part of your complex number: "))
    imaginaryNumber = float(input("Enter the imaginary part of your complex number: "))
    return realNumber, imaginaryNumber


def addition(real1, real2, imaginary1, imaginary2):
    return real1+real2, imaginary1+imaginary2


def subtraction(real1, real2, imaginary1, imaginary2):
    return real1-real2, imaginary1-imaginary2


def multiply(real1, real2, imaginary1, imaginary2):
    return (real1*real2)-(imaginary1*imaginary2), (real1*imaginary2)+(real2*imaginary1)


def divide(real1, real2, imaginary1, imaginary2):
    denominator = real2 ** 2 + imaginary2 ** 2
    realQuotient = (real1*real2 + imaginary1*imaginary2)/denominator
    imaginaryQuotient = (imaginary1*real2 - real1*imaginary2)/denominator
    return realQuotient, imaginaryQuotient


if __name__ == "__main__":
    main()