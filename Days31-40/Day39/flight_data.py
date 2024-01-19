from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

#This class is responsible for structuring the flight data.
class FlightData:
  def __init__(self):
    self.dataManager = DataManager()
    self.flightSearch = FlightSearch()
    self.notificationManager = NotificationManager()

    self.gSheetPrices = []

  def checkPricetoSheet(self):
    
    gSheetData = self.dataManager.getSheetData()
    for destination in range(len(gSheetData)):
      self.gSheetPrices.append(gSheetData[destination]["lowestPrice"])

    for id in range(len(gSheetData)):
      self.flightSearch.getSearchData(str(gSheetData[id]["iataCode"]))
    lowPriceList = self.flightSearch.lowestPriceList
    print(self.flightSearch.travelDates)

    for price in range(len(self.gSheetPrices)):
      if self.gSheetPrices[price] > lowPriceList[price]:
        self.notificationManager.sendEmail(city=gSheetData[price]["city"], iata=gSheetData[price]["iataCode"], price=lowPriceList[price], flightSearchData=self.flightSearch.travelDates)

        self.dataManager.putSheetData(newLow=lowPriceList[price], id=gSheetData[price]["id"])
      
      else:
        self.dataManager.putSheetData(newLow=lowPriceList[price], id=gSheetData[price]["id"])