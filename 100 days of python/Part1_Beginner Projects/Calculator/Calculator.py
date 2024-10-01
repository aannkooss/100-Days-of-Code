#Ankush Joshi
#August 14, 2024
#10/100 - Calculator
#Topic: Functions with outputs
from asciiart import calculator

def add(num1, num2):
    return num1+num2

def subtract(num1,num2):
    return num1-num2

def divide(num1, num2):
    return num1/num2

def multiply(num1,num2):
    return num1*num2

operations = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply
}

def calc():
    print(calculator[0]+calculator[1])
    shouldAccumulate = True
    num1 = float(input("Enter the first number: "))
    while shouldAccumulate:
        operation = input("Choose an operation: (+ - / *) ")
        num2 = float(input("Enter the second number: "))
        answer = operations[operation](num1,num2)

        print(f"{num1} {operation} {num2} = {answer}")

        choice = input(f"Type 'y' to continue with {answer} or 'n' to restart ").lower()

        if choice == 'y':
            num1 = answer
        elif choice == "n":
            shouldAccumulate = False
            print("\n"*20)
            calc()
        else:
            print("Please enter 'y' or 'n'")

calc()