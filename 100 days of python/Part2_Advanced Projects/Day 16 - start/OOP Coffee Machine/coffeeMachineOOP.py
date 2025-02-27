#Ankush Joshi
#September 14, 2024
#Day 16/100 - Coffee Machine - OOP

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

validChoices = {"espresso", "latte", "capuccino", "report", "off"}

#declaring variables of <Object> Type
coffeeMaker = CoffeeMaker()
menu = Menu()
moneyMachine = MoneyMachine()

isOn = True

while isOn:
    options = menu.get_items()
    drink = input(f"What would you like? ({options}): ").lower()
    while drink not in validChoices:
        drink = input("Please enter a valid option as you see it: ")

    if drink == "report":
        coffeeMaker.report()
        moneyMachine.report()
    elif drink == "off":
        isOn = False
        print("Goodbye")
    else:
        drinkName = menu.find_drink(drink) #menu is a Menu object, so we can use its functions. DrinkName gets the information
        if coffeeMaker.is_resource_sufficient(drinkName) and moneyMachine.make_payment(drinkName.cost): #checks if there is enough ingredients using the attributes from drinkName
            coffeeMaker.make_coffee(drinkName)