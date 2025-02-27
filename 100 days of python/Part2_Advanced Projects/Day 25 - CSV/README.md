Day 25 - Read CSV and Pandas Library 

CSV stands for Comma Separated List and essentially is just a file with a table data  

Start by importing CSV library with `import csv`  
- csv has its own built in functions as well  

Pandas library gives more access to bigger data sets with `import pandas`  
// useful functions  
- `data = pandas.read_csv("dataFile.csv")` - reads and stores csv into data
- `print(data)` - prints entire data table
- `print(data["<columnName>"])` or `print(data.columnName`- prints desired column
  - note: Series are coluns and DataFrames are the entire data set  
- `print(data["name"].to_list)` converts data column into a list/array  

PRACTICE ACTIVITY:  
The practice activity was to use a very large file and return a data frame of just the 
amount of squirrel colors in a set into a csv file 

Steps: 
- import panda library `import pandas`
- read data into file `data = pandas.read_csv("data.csv")`
- get squirrel colors `data[data["Primary Fur Color] == "color"]`
  - get squirrel color count `len(<function above>)`
- convert into dictionary `dataDictionary = {"Header": ["elements", "elements",...], ...}`
- convert dictionary into dataFrame `dataFrame = pandas.DataFrame(dataDictionary)`
- Convert DataFrame into .csv `dataFrame.to_csv("name.csv")`

