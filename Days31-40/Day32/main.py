##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv ✅

# 2. Check if today matches a birthday in the birthdays.csv ✅

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv ✅

# 4. Send the letter generated in step 3 to that person's email address. ✅

import datetime as dt
import os
import random
import smtplib
import pandas
scriptDirectory = os.path.dirname(__file__)
# ---------- EMAIL VARIABLES ---------- #
gmail = "smtp.gmail.com"
myEmail = "johnerr370@gmail.com"
appPassword = "wdvcujfdcslygzwa"
testEmail = "garrhj2464@outlook.com"

# ---------- DATE/TIME VARIABLES ---------- #
dayOfMonth = dt.datetime.now().day
monthOfYear = dt.datetime.now().month

birthdaysFile = pandas.read_csv(f"{scriptDirectory}\\birthdays.csv")
birthdaysDict = birthdaysFile.to_dict()

# How to find the index of a specific value in a column.
# print(FILE[FILE['COLUMN'] == VALUE].index.values[0])

index = 0

if dayOfMonth in birthdaysDict["day"].values() and monthOfYear in birthdaysDict["month"].values():
  index = birthdaysFile[birthdaysFile['month'] == monthOfYear].index.values[0] and birthdaysFile[birthdaysFile['day'] == dayOfMonth].index.values[0]
  print("Good")
  bDayName = birthdaysDict["name"][index]

  with open(f"{scriptDirectory}\\letter_templates\\letter_{random.randint(1,3)}.txt") as bDayLetterFile:
    bDayLetterContents = bDayLetterFile.read().replace("[NAME]", bDayName)
  
  with smtplib.SMTP(gmail, port=587) as connection:
    connection.starttls()
    connection.login(user=myEmail, password=appPassword)
    connection.sendmail(from_addr=myEmail, to_addrs=testEmail,
                        msg=f"Subject:Happy Birthday!.\n\n{bDayLetterContents}")
