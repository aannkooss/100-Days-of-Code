# # Traditional way of opening files
# # with open("weather_data.csv") as weatherData:
# #     data = weatherData.readlines()
# #     for dataPoints in data:
# #         strippedData = dataPoints.strip()
# #         print(strippedData)
#
# # A better way of opening files, specific to CSV
# # import csv
# #
# # with open("weather_data.csv") as dataFile:
# #     data = csv.reader(dataFile)
# #     print(data) #prints reader object which can be looped through (next line)
# #     temperature = []
# #     for row in data:
# #         if row[1] != "temp": #excludes header
# #             temperature.append(int(row[1])) #directly appends the numbers
# #
# #     print(temperature)
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")  #this replaces the first two lines of the top chunk
# # print(data) #prints the whole table
# # print(type(data)) #prints the data type of parameter: <class 'pandas.core.frame.DataFrame'>
# # print(data["temp"]) # prints temp column only
#
# # -- Series type is column. DataFrame type is entire table essentially
#
# #dataDict = data.to_dict()
# #print(dataDict)
#
# #tempList = data["temp"].to_list()
# #print(tempList)
#
# # average = sum(tempList) / len(tempList)
# # roundAverage = round(average, 2)
# # print(roundAverage)
#
# data["temp"].mean()  #does the same as finding average above
# # print(data["temp"].max()) #gets max value of Series (column)
#
# # print(data.condition) #an alternative to using data["name"] - CASE SENSITIVE
# # print(data[data.day == "Monday"]) #prints Row where Day = Monday
#
# #Print the row which has the highest temperature
#
# max = data.temp.max()
# print(data[data.temp == max])  # will print the row that has the max temperature
#
# monday = data[data.day == "Monday"]
# monTemp = monday.temp[0] #this grabs the first (temperature) element only
# monTempF = (monTemp * 9 / 5) + 32
# print(monTempF) # prints temperature, without row number
#
# # Create a Data Frame from Scratch
# dataDict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [75, 56, 65]
# }
#
# data = pandas.DataFrame(dataDict)
# data.to_csv("newData.csv")

# -------------------------------------------------

import pandas
# Read Data from csv
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# Get data: data[data["Primary Fur Color"] == "Gray"] gives row of grey squirrels. len() returns length
greySquirrels = len(data[data["Primary Fur Color"] == "Gray"])
cinnamonSquirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
blackSquirrels = len(data[data["Primary Fur Color"] == "Black"])

#initialize a dictionary
dataDict = {
    "Fur Color": ["Grey", "Cinnamon", "Black"], #create header with elements
    "Count":     [greySquirrels, cinnamonSquirrels, blackSquirrels] #using entries directly to make code modular
}

data = pandas.DataFrame(dataDict) # Converting the dictionary into a dataFrame
data.to_csv("Squirrel_Count.csv") # Converting dataFrame into a .csv file