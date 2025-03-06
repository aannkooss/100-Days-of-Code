
try:
    file = open("aFile.txt")
    aDictionary = {"key" : "value"}
    print(aDictionary["key"])
except FileNotFoundError: # If the line above fails, execute following line
    file = open("aFile.txt", "w") # opening in "w" mode creates the file
    file.write("Something")
except KeyError:
    print("That key does not exist")
else:
    content = file.read()
    print(content)
finally: # will execute no matter what happens
    file.close()
    print("file closed")

    raise KeyError # allows us to raise our own exceptions


# ## Example
#
# height = float(input("Height: "))
# weight = float(input("Weight: "))
#
# if height > 3: # ensures the user does not input an unrealstic height greater than 3m
#     raise ValueError("Human height should not be over 3 meters")
#
# bmi = weight / height ** 2

