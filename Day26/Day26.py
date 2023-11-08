import random
import pandas

# List Comprehension.--------
# newList = [newItem for item in numbers]

# numbers = [1, 2, 3]
# newList = [n + 1 for n in numbers]
# print(newList)

# name = "Joseph"
# lettersList = [letter for letter in name]
# print(lettersList)

# rangeList = [n * 2 for n in range(1, 5)]
# print(rangeList)

# Conditional List Comprehension.--------
# newList = [newItem for item in list if test]

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# shortNames = [name for name in names if len(name) < 5]
# print(shortNames)

# longNamesCapital = [name.upper() for name in names if len(name) > 4]
# print(longNamesCapital)

# Dictionary Comprehension.--------
# newDict = {newKey:newValue for item in list if test}

# Can be used with a existing dict as well.             v---The .items() is needed for this to work.
# newDict = {newKey:newValue for (key,value) in dict.items() if test}

# studentScores = {student:random.randint(1,100) for student in names}
# print(studentScores)

# passedStudents = {student:score for (student, score) in studentScores.items() if int(score) >= 60}
# print(passedStudents)

# # Challenge-------- Add the input into a dict by adding each word and the len of the word as the key:value.
# sentence = input() # What is the Airspeed Velocity of an Unladen Swallow?
# # 🚨 Don't change code above 👆
# # Write your code below 👇

# result = {word:len(word) for word in sentence.split()}

# print(result)

# # Challenge-------- Take the input of a day and temperature in Celsius and convert the temperature into Fahrenheit.
# #            V------ eval() looks at the format and converts it accordingly.
# weather_c = eval(input()) #{"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
# # 🚨 Don't change code above 👆
# # Write your code 👇 below:
# # F = (C x 1.8) + 32
# weather_f = {day:(temp*1.8)+32 for (day, temp) in weather_c.items()}

# print(weather_f)

# Loop through rows of a data frame with Pandas.
studentsDict = {
  "student": ["Tabi", "Joe", "George", "Gromit"],
  "score": [98, 80, 88, 75],
}
studentDataFrame = pandas.DataFrame(studentsDict)
print(studentDataFrame)

for (index, row) in studentDataFrame.iterrows():
  print(row.student)

# If statements can be used.
for (index, row) in studentDataFrame.iterrows():
  if row.student == "Tabi":
    print(row.score)