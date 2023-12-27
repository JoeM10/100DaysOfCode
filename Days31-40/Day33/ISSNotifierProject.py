import requests
from datetime import datetime
import smtplib

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

gmail = "smtp.gmail.com"
myEmail = "johnerr370@gmail.com"
appPassword = "wdvcujfdcslygzwa"
testEmail = "garrhj2464@outlook.com"

def isISSClose():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    
    return MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5

#Your position is within +5 or -5 degrees of the ISS position.

def isNightTime():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    
    return time_now < sunrise or time_now > sunset

if isISSClose() == True and isNightTime() == True:
    with smtplib.SMTP(gmail, port=587) as connection:
        connection.starttls()
        connection.login(user=myEmail, password=appPassword)
        connection.sendmail(from_addr=myEmail, to_addrs=testEmail, 
                            msg=f"Subject:ISS Overhead Notifier.\n\nLook Up!!!")

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



