# with open("myFile.txt") as file: #equivalent to file = open(<file_name>)
#     contents = file.read()
#     print(contents)

    #file.close() this line is no longer needed when using "with" keyword

# ----- modes: "w" is write (replaces text), "a" adds to the file

# ---- opening a file in write mode when it doesnt already exist -> creates the file if it doesnt exist and writes to it
# with open("newFile.txt", mode="w") as file:
#     file.write("New Text")

# ----- opening a file located in a different directory
#open(file path + filename.txt in quotes)

with open("C:/Users/ankus/Desktop/myFile.txt") as file:
    contents = file.read()
    print(contents)


#rest of day done as an implementation of a high score feature in snake (day 20/21)