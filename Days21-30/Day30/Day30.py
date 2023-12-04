import os
scriptDirectory = os.path.dirname(__file__)

# Learning about exceptions and errors.

#FileNotFound
# with open("aFile.txt") as file:
#   file.read()

# KeyError
# aDictionary = {"key": "value"}
# value = aDictionary["nonExistentKey"]

# IndexError
# fruitList = ["Apple", "Banana", "Pear"]
# fruit = fruitList[3]

# TypeError
# text = "abc"
# print(text + 5)

# try except keywords.

# try: something that might cause an exception.
# except: do this if there was an exception. You can have multiple exceptions.
# else: do this if there were no exceptions.
# finally: do this no matter what happens.

# try:
#   file = open(f"{scriptDirectory}\\aFile.txt")
#   aDictionary = {"key": "value"}
#   print(aDictionary["key"])
# except FileNotFoundError:
#   file = open(f"{scriptDirectory}\\aFile.txt", "w")
#   file.write("Something")
# except KeyError as error_message:
#   print(f"The key {error_message} does not exist.")
# else:
#   content = file.read()
#   print(content)
# finally:
#   file.close()
#   print("File was closed.")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
  raise ValueError("Human Height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)