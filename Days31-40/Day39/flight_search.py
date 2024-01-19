#This class is responsible for talking to the Flight Search API.
import os
import requests
from datetime import datetime, timedelta
from data_manager import DataManager
# ---------- CONSTANTS ---------- #
TEQUILA_FLIGHT_API_KEY = str(os.environ.get("TEQUILA_FLIGHT_API_KEY"))
TEQUILA_ENDPOINT =  "https://api.tequila.kiwi.com/v2/search"

class FlightSearch:
  def __init__(self):
    self.lowestPriceList = []
    self.travelDates = {}

  def getSearchData(self, iata:str):
    now = datetime.now()
    todaysDate = str(now.strftime("%d/%m/%Y"))
    dateInSixMonths = str((now + timedelta(days=6*30)).strftime("%d/%m/%Y"))
    
    tequilaHeader = {
      "apikey": TEQUILA_FLIGHT_API_KEY
    }

    tequilaParams = {
      "fly_from": "PDX",
      "fly_to": iata,
      "date_from": todaysDate,
      "date_to": dateInSixMonths,
      "nights_in_dst_from": 3,
      "nights_in_dst_to": 12,
      "adults": 1,
      "curr": "USD",
    }
    tequilaGetResponse = requests.get(url=TEQUILA_ENDPOINT, params=tequilaParams, headers=tequilaHeader)
    tequilaGetResponse.raise_for_status()

    tequilaJsonData = tequilaGetResponse.json()
    tequilaData = tequilaJsonData["data"]
    lowestFare = tequilaData[0]["price"]
    for flight in range(len(tequilaData)):
      if tequilaData[flight]["price"] < lowestFare:
        lowestFare = int(tequilaData[flight]["price"])
        self.travelDates.update({f"{iata}_departure":tequilaData[flight]["local_departure"].strftime("%d/%m/%Y"),
                                 f"{iata}_arrival":tequilaData[flight]["local_arrival"].strftime("%d/%m/%Y")})
    self.lowestPriceList.append(lowestFare)