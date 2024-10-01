from car import Car

print("Please enter a car, you will need to fill out a make, model, year and color") #user created car
userMake = input("Make: ")
userModel = input("Model: ")
userYear = int(input("Year: "))
userColor = input("Color: ")
userCar = Car(userMake, userModel, userYear, userColor)

#car1 = Car("Ford","Focus",2014,"White")
#car2 = Car("Toyota","Camry",2019,"Black")

#print(userCar.make)
#print(userCar.model)
#print(userCar.year)
#print(userCar.color)

#userCar.drive()
#userCar.stop()

print("Your car is a", userCar.color, userCar.year,userCar.make,userCar.model)