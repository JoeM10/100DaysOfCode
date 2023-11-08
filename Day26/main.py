import pandas
import os

scriptDirectory = os.path.dirname(__file__)
natoData = pandas.read_csv(f"{scriptDirectory}\\nato_phonetic_alphabet.csv")
# print(natoData)

student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
# for (key, value) in student_dict.items():
    #Access key and value
    # print(key, value)

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

#Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    # print(f"This is the index\n{index}")
    # print(f"This is the row\n{row}")

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
natoDict = {row.letter:row.code for (index, row) in natoData.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
lettersList = [letter for letter in str(input()).upper()]
outputList = [natoDict[letter] for letter in lettersList]
print(outputList)