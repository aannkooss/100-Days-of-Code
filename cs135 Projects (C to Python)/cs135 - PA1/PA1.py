#Ankush Joshi
#June 23, 2024
#CS135 PA1 - Python

print("\nWelcome to Jae's Flower Shop!\n" + "Here is a list of all the flowers we have in stock! Feel Free to take a "
                                            "look and order whenever you're ready!\n")
print("         |**\\JAE'S FLOWERS/**|")
print("--Rose: $1.49 | Color: R | IN STOCK--")
print("--Iris: $1.99 | Color: V | IN STOCK--")
print("--Lily: $2.50 | Color: O | IN STOCK--")
print("\nPlease Fill out the order sheet, with the amount of flowers you would like")

quantity1 = input("How many Roses? ")
quantity2 = input("How many Irises? ")
quantity3 = input("How many Lilies? ")

print("Here is your order")
print("\nROSES: " + quantity1 + " at $1.49 per flower | Total: $" + str(float(quantity1)*1.49))
print("IRIS: " + quantity2 + " at $1.99 per flower | Total: $" + str(float(quantity2)*1.99))
print("LILIES: " + quantity3 + " at $2.50 per flower | Total: $" + str(float(quantity3)*2.50))
total = float(quantity1)*1.49 + float(quantity2)*1.99 + float(quantity3)*2.50
print("\nYour total comes out to: $" + str(total))
