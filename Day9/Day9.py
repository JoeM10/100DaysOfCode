import os
# 
# Learning about dictionarys
# 
'''
programmingDictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.", #<--- It's a good habit to end the last item in a dictionary with a ,
}
# Adding new items to a dictionary.
programmingDictionary["Loop"] = "The action of doing something over and over again."
print(programmingDictionary)

# Wipe and existing dictionary.
programmingDictionary = {}
print(programmingDictionary)

# Edit a existing item in a dictionary.
programmingDictionary["Bug"] = "A moth in your computer."
print(programmingDictionary)

# Loop through a dictionary.
for thing in programmingDictionary:
    print(thing) #<--- This will print the key names only. ex: Bug
    print(programmingDictionary[thing]) #<--- This will print only the value. ex:"A moth in your computer."

# You can nest lists inside of a dictionary.
travelLog = {
    "Iceland": ["Reykjavik", "Akureyri", "Isafjordur"],
    "Japan": ["Tokyo", "Kyoto", "Osaka"],
}

# You can also nest other dictionaries inside one another.
travelLog = {
    "Iceland": {"citiesVisited": ["Reykjavik", "Akureyri", "Isafjordur"], "totalVisits": 2},
    "Japan": {"citiesVisited": ["Tokyo", "Kyoto", "Osaka"], "totalVisits": 1},
}

# You can nest a dictionary inside a list.
travelLog = [
    {
        "country": "Iceland",
        "citiesVisited": ["Reykjavik", "Akureyri", "Isafjordur"],
        "totalVisits": 2
    },
    {
        "country": "Japan",
        "citiesVisited": ["Tokyo", "Kyoto", "Osaka"],
        "totalVisits": 1
    },
]
# Spacing things out like that makes it easier to read.

# 
# Grading Program Project
# 

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.

student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇

for studentName in student_scores:
    if student_scores[studentName] > 90:
        student_grades[studentName] = str("Outstanding")

    elif student_scores[studentName] > 80 and student_scores[studentName] <= 90:
        student_grades[studentName] = str("Exceeds Expectations")

    elif student_scores[studentName] > 70 and student_scores[studentName] <= 80:
        student_grades[studentName] = str("Acceptable")

    else:
        student_grades[studentName] = str("Fail")    

# 🚨 Don't change the code below 👇
print(student_grades)

# 
# Dictionary in list Challenge.
# 

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country, visits, cities):
    newCountry = {
        "country": country,
        "visits": visits,
        "cities": cities,
    }
    travel_log.append(newCountry)

#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
'''
# 
# Silent Auction Program
# 
import art
restart = False
print(art.logo)

participants = []

def userInfo(name, bidPrice):
    newUser = {
        "name": name,
        "bid": int(bidPrice),
    }
    participants.append(newUser)

while restart == False:
    name = str(input("What is your name?\n"))

    while True:
        bidPrice = input("What is your bid price?\n$")
        if bidPrice.isdigit():
            bidPrice = int(bidPrice)
            break
        else:
            print("Invalid input. Please use only numbers in your bid price.")

    userInfo(name, bidPrice)

    while True:
        goAgain = input("Is there more participants in the auction? 'yes' or 'no'\n")
        if goAgain == "yes":
            os.system('cls')
            break
        elif goAgain == "no":
            restart = True
            os.system('cls')
            break
        else:
            print("Invalid input. Please type 'yes' or 'no'")
sortedParticipants = sorted(participants, key=lambda x: x["bid"], reverse=True)

print(f"The winner of the auction is {sortedParticipants[0]['name']} for ${sortedParticipants[0]['bid']}.")