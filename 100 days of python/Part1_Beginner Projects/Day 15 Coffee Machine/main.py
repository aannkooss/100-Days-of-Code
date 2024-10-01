MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

validChoices = {
    "espresso", "latte", "cappuccino", "report"
}
profit = 0

def insertCoins():
    total = 0
    print("Please insert coins")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))

    total += quarters*0.25 + dimes*0.1 + nickles*0.5 + pennies*0.01
    return total

def enoughIngredients(order):
    for item in order:
        if order[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def transactionSuccess(payment, cost):
    if payment >= cost:
        change = round(payment - cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += cost
        return True
    else:
        print("Sorry that is not enough money. Money refunded")
        return False

def makeCoffee(drink, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink}. Enjoy!")

isOn = True

while isOn:
    userChoice = input("What would you like? (espresso/latte/capuccino) ").lower()

    while userChoice not in validChoices:
        userChoice = input("Sorry, please pick one of the available options - Espresso, latte, cappuccino. "
                           "(Type it exactly as you see it) ")

    if userChoice == "report":
        print(f"Water: {resources["water"]}mL")
        print(f"Milk: {resources["milk"]}mL")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[userChoice]
        if enoughIngredients(drink["ingredients"]):
            payment = insertCoins()
            if transactionSuccess(payment, drink["cost"]):
                makeCoffee(userChoice, drink["ingredients"])
