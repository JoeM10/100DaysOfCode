#This class is responsible for talking to the Google Sheet.
import os
import requests
# ---------- CONSTANTS ---------- #
SHEETY_API_KEY = os.environ.get("SHEETY_API_KEY")
SHEETY_AUTH = (str(os.environ.get("SHEETY_USERNAME")), str(os.environ.get("SHEETY_PASSWORD")))
SHEETY_PRICES_ENDPOINT = f"https://api.sheety.co/{SHEETY_API_KEY}/flightDealsProject/prices"

class DataManager:
  def __init__(self):
    self.sheetyData = {}

  def getSheetData(self):
    sheetyGetResponse = requests.get(url=SHEETY_PRICES_ENDPOINT, auth=SHEETY_AUTH)
    sheetyGetResponse.raise_for_status()
    sheetyResponseData = sheetyGetResponse.json()
    self.sheetyData = sheetyResponseData["prices"]
    return self.sheetyData

  def putSheetData(self, newLow:int, id:int):
    putSheetyData = {
      "price": {
        "lowestPrice": newLow,
      }
    }

    sheetyPutResponse = requests.put(url=f"{SHEETY_PRICES_ENDPOINT}/{id}", json=putSheetyData, auth=SHEETY_AUTH)
    sheetyPutResponse.raise_for_status()
    print("response.status_code=", sheetyPutResponse.status_code)
    print("response.text=", sheetyPutResponse.text)
