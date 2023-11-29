#Study Stuff

#When using the print statement, \n will put whatever is after it onto a new line without having to make multiple print statements. P.S.-No spaces between \n
#ex: print("Hello World!\nHello World!")
#    Hello World!
#    Hello World!

#To have the input come up in terminal next to the question text, rather than below it, write it this way.

#print(input('What is your name? '))
#This will have a outcome of:
#What is your name? <---The input will be put here rather than on another line.

#If you want the length of the name inputed just put len before input.

#print(len(input('What is your name? ')))

#Band Name Generator Project

print('Welcome to the Band Name Generator!')

print('What is the name of the city you grew up in?')

city = input(str())

print('What is the name of a pet you have?')

pet = input(str())

print('Heres your new band name! '+city+pet)