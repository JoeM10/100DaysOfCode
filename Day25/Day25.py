import os
import csv
import pandas

scriptDirectory = os.path.dirname(__file__)

# # with open(f"{scriptDirectory}\\weather_data.csv") as weatherFile:
# #   weatherData = weatherFile.readlines()
# #   print(weatherData)

# # Importing and using csv will allow you to use csv.reader() which organizes the csv data.
# # with open(f"{scriptDirectory}\\weather_data.csv") as weatherFile:
# #   weatherData = csv.reader(weatherFile)
# #   # print(weatherData) # - This will print a csv.reader object. To print the data, use a loop.
# #   for row in weatherData:
# #     print(row)

# with open(f"{scriptDirectory}\\weather_data.csv") as weatherFile:
#   weatherData = csv.reader(weatherFile)
#   temperatures = []
#   for row in weatherData:
#     if row[1] != "temp":
#       temperatures.append(int(row[1]))
#   print(temperatures)

# # Pandas will automatically sort data into collumns.
# # You can retrieve whole collumns by just specifying the name of the collumn.
# data = pandas.read_csv(f"{scriptDirectory}\\weather_data.csv")
# print(data["temp"])

# # If you wanted the contents of the CSV file to be put into a dictionary for use in Python.
# dataDict = data.to_dict()
# print(dataDict)

# # If you wanted a collumn of the CSV file to be put into a list for use in Python.
# tempList = data["temp"].to_list()
# print(tempList)

# # Pandas has a lot of built in functions for dealing with data.
# averageTemp = data["temp"].mean()
# print(averageTemp)

# highestTemp = data["temp"].max()
# print(highestTemp)

# # Pandas will allow you to call callumns like this as well.
# print(data.temp)

# # Get data in Row.
# print(data[data.day == "Monday"])

# print(data[data.temp == data.temp.max()])

# mondayTempinFahrenheit = (data.temp[data.day == "Monday"] * 1.8) + 32
# print(mondayTempinFahrenheit)

# # Create dataframe from scratch.
# dataDict = {
#   "students": ["Amy", "James", "Angela"],
#   "scores": [76, 56, 65]
# }
# newDataFrame = pandas.DataFrame(dataDict)

# # You can convert a dataframe into a CSV file. The function takes the path you want it to save to as the argument.
# newDataFrame.to_csv(f"{scriptDirectory}\\newDataCSV.csv")

# ---Challenge--- Get the count of squirrels sperated by color and put into a new CSV file.
squirrelData = pandas.read_csv(f"{scriptDirectory}\\SquirrelData.csv")

graySquirrel = len(squirrelData[squirrelData["Primary Fur Color"] == "Gray"])
cinnamonSquirrel = len(squirrelData[squirrelData["Primary Fur Color"] == "Cinnamon"])
blackSquirrel = len(squirrelData[squirrelData["Primary Fur Color"] == "Black"])

squirrelDict = {
  "Fur Color": ["Gray", "Cinnamon", "Black"],
  "Count": [graySquirrel, cinnamonSquirrel, blackSquirrel]
}
squirrelDataFrame = pandas.DataFrame(squirrelDict)
squirrelDataFrame.to_csv(f"{scriptDirectory}\\SquirrelCount.csv")