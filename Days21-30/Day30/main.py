# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
#ToDo 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)

#ToDo 2. Create a list of the phonetic code words from a word that the user inputs.
trying = True
while trying:
  try:
    word = input("Enter a word: ").upper()
    output_list = [phonetic_dict[letter] for letter in word]
  except KeyError:
    print("Sorry, only letters in the alphabet please.")
  else:
    print(output_list)
    trying = False