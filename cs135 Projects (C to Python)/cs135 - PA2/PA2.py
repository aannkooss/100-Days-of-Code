#Ankush Joshi
#June 23, 2024
#CS135 PA2 - Python

discount = 0.03

print("\nWelcome Back to Jae's Flower Shop!")
print("Today's your special day! We are having a special deal where you are given a 3% discount for every flower you "
      "buy over 6 flowers!\n")
print("        |**\\JAE'S FLOWERS/**|")
print("--Rose: $4.99 | Color: R | IN STOCK--")
print("--Iris: $2.99 | Color: V | IN STOCK--")
print("--Lily: $1.75 | Color: O | IN STOCK--")

print("\nAll set? Lets begin your order... in the following prompts, please enter the amount of flowers and the color"
      "(Ex: 8 R, for 8 red flowers)")
userChoice1 = input("Please Enter the number of flowers and color (R,V,O): \n" + ">")
numFlowers1, color1 = userChoice1.split()
numFlowers1 = int(numFlowers1)

print("\nGreat! Lets move on to the next order...")
userChoice2 = input("Please enter the number of flowers and color (R,V,O) of the second flower: \n" + ">")
numFlowers2, color2 = userChoice2.split()
numFlowers2 = int(numFlowers2)

if color1 == "R" or color1 == "r":
    price1 = 4.99
elif color1 == "V" or color1 == "v":
    price1 = 2.99
elif color1 == "O" or color1 == "O":
    price1 = 1.75
else:
    "invalid entry"
    price1 = 0

if color2 == "R" or color2 == "r":
    price2 = 4.99
elif color2 == "V" or color2 == "v":
    price2 = 2.99
elif color2 == "O" or color2 == "o":
    price2 = 1.75
else:
    "invalid entry"
    price2 = 0


priceBeforeDiscount1 = price1 * numFlowers1
discountPrice1 = (numFlowers1 - 6) * discount
if numFlowers1 <= 6:
    totalPrice1 = price1 * numFlowers1
else:
    if discountPrice1 >= 0.5:
        discountPrice1 = 0.5

discountPrice1 = (numFlowers1 - 6) * discount
priceAfterDiscount1 = priceBeforeDiscount1 - (priceBeforeDiscount1 * discountPrice1)


priceBeforeDiscount2 = price2 * numFlowers2
discountPrice2 = (numFlowers2 - 6) * discount
if numFlowers2 <= 6:
    totalPrice2 = price2 * numFlowers2
else:
    if discountPrice2 >= 0.5:
        discountPrice2 = 0.5

discountPrice2 = (numFlowers2 - 6) * discount
priceAfterDiscount2 = priceBeforeDiscount2 - (priceBeforeDiscount2 * discountPrice2)

print("\n /**\\ FLOWER SHOP ORDERS /**\\")
print("====================================")
print("| FLOWERS | QUANTITY | PRICE TOTAL |")
print("------------------------------------")
print(f"|{color1:^9}|{numFlowers1:^9}|    ${priceAfterDiscount1:.2f}    |")
print("------------------------------------")
print(f"|{color2:^9}|{numFlowers2:^9}|    ${priceAfterDiscount2:.2f}    |")
print("====================================")

if priceAfterDiscount1 < priceAfterDiscount2:
    print("The " + color1 + " flower order for $" + str(priceAfterDiscount1) + " is the better deal")
elif priceAfterDiscount1 > priceAfterDiscount2:
    print("The " + color2 + " flower order for $" + str(priceAfterDiscount2) + " is the better deal")
else:
    print("These flowers are the same price, you choose!")
