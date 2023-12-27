import requests
import datetime
# ---------- RESPONSE CODES ---------- #
# 1XX : Hold On
# 2XX : Here You Go
# 3XX : Go Away
# 4XX : You Screwed Up
# 5XX : I Screwed Up

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status() # .raise_for_status() will automatically handle error Exceptions and raise them.

# longitude = response.json()["iss_position"]["longitude"]
# latitude = response.json()["iss_position"]["latitude"]

# issPosition = (longitude, latitude)
# print(issPosition)

parameters = {
  "lat": 46.169509,
  "lng": -123.010253,
  "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
sunrise = response.json()["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = response.json()["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)