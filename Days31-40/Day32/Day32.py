import smtplib
import datetime as dt
import os
import random
scriptDirectory = os.path.dirname(__file__)

# # DATETIME
# now = dt.datetime.now()
# year = now.year
# month = now.month
# dayOfWeek = now.weekday()
# print(now)
# print(year)
# day = dt.datetime.now().day

# # SMTP INFORMATION
gmail = "smtp.gmail.com"
hotmail = "smtp.live.com"
yahoo = "smtp.mail.yahoo.com"

myEmail = "johnerr370@gmail.com"
appPassword = "wdvcujfdcslygzwa"

testEmail = "garrhj2464@outlook.com"

# # SENDING A EMAIL WITH GMAIL
# with smtplib.SMTP(gmail, port=587) as connection:
#   connection.starttls()
#   connection.login(user=myEmail, password=appPassword)
#   For the subject/body of the email, msg="Subject:THIS IS THE SUBJECT\n\nTHIS IS THE BODY"
#   connection.sendmail(from_addr=myEmail, to_addrs=testEmail, 
#                       msg="Subject:Hello\n\nThis is the body of my email.")

# Motivational Quote Project
with open(f"{scriptDirectory}\\quotes.txt", mode="r") as file:
  quotes = file.readlines()
quoteOfTheDay = random.choice(quotes)

currentDateTime = dt.datetime.now()
dayOfWeek = currentDateTime.weekday()

if dayOfWeek == 4:
  with smtplib.SMTP(gmail, port=587) as connection:
    connection.starttls()
    connection.login(user=myEmail, password=appPassword)
    connection.sendmail(from_addr=myEmail, to_addrs=testEmail, 
                        msg=f"Subject:Motivational Quote of the Day.\n\n{quoteOfTheDay}")