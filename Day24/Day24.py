import os

# # You can use "cd PATH/YOU/WANT/TO/USE" in the Terminal to set a cwd.

# # Gives you your current working directory.
# currentDirectory = os.getcwd()

# # This will give you the directory of the file the script was ran in.
# scriptDirectory = os.path.dirname(__file__)

# # with open("myFile.txt") as file:
# #   contents = file.read()

# # Append something to a file.
# with open(f"{currentDirectory}\\myFile.txt", mode="a") as file:
#   file.write("\nNew text.")

# # Overwrite everything in a file with something else.
# with open("newFile.txt", mode="w") as file:
#   file.write("New text.")

# # Absolute path.
# with open("C:\\Code_Stuff\\100DaysOfCode\\Day21\\data.txt") as file:
#   contents = file.read()
#   print(contents)

# # Using ""..\\" will go back 1 folder in the directory allowing you to use relative path tracing.
# with open("..\\Day21\\data.txt") as file:
#   contents = file.read()
#   print(contents)

#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

scriptDirectory = os.path.dirname(__file__)

with open(f"{scriptDirectory}\\Input\\Letters\\starting_letter.txt", mode='r') as startingFile:
  startingLetter = startingFile.readlines()
letterStr = ""
for line in startingLetter:
  letterStr += line

with open(f"{scriptDirectory}\\Input\\Names\\invited_names.txt", mode='r') as namesFile:
  namesBeforeStrip = namesFile.readlines()
names = []

for name in namesBeforeStrip:
  name = name.strip("\n")
  names.append(name)

for name in names:
  with open(f"{scriptDirectory}\\Output\\ReadyToSend\\InviteFor{name}.txt", mode='w') as inviteFile:
    newName = name
    withName = letterStr.replace('[name]', newName)
    inviteFile.write(withName)
