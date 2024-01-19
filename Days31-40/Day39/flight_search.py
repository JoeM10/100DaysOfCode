#This class is responsible for talking to the Flight Search API.
import os
import requests
from datetime import datetime, timedelta
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
    lowestFare = 10000
    for flight in range(len(tequilaData)):
      if tequilaData[flight]["price"] < lowestFare:
        lowestFare = int(tequilaData[flight]["price"])

        departure_datetime = datetime.strptime(tequilaData[flight]["local_departure"], "%Y-%m-%dT%H:%M:%S.%fZ")
        formatted_departure = departure_datetime.strftime("%d/%m/%Y")

        arrival_datetime = datetime.strptime(tequilaData[flight]["local_arrival"], "%Y-%m-%dT%H:%M:%S.%fZ")
        formatted_arrival = arrival_datetime.strftime("%d/%m/%Y")

        self.travelDates.update({f"{iata}_departure":formatted_departure,
                                 f"{iata}_arrival":formatted_arrival})
    self.lowestPriceList.append(lowestFare)