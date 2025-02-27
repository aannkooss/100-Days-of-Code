studentDict = {
    "student": ['Angela', 'James', "lily"],
    "score": [56, 76, 98]
}

for (key, value) in studentDict.items():
    print(value) #will print everything inside lists
    print(key) # will print student and score

import pandas

studentDataFrame = pandas.DataFrame(studentDict)
print(studentDataFrame)

# Loop through a data frame

# for (key,value) in studentDataFrame.items():
#     print(key)

# Loop through rows of a data frame

for (index, row) in studentDataFrame.iterrows():
    if row.student == "Angela":
        print(row.score)