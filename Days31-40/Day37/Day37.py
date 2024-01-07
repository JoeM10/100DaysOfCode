import requests
import os
from datetime import datetime

# ---------- CONSTANTS ---------- #
PIXELA_TOKEN = os.environ.get("PIXELA_TOKEN")
PIXELA_USERNAME = os.environ.get("PIXELA_USERNAME")
GRAPH = "graph1"

# ---------- VARIABLES ---------- #
todaysDate = datetime.now()
formattedTodaysDate = todaysDate.strftime("%Y%m%d")

pixelaEndpoint = "https://pixe.la/v1/users"

# ---------- CREATING A USER ---------- #
userParams = {
  "token": PIXELA_TOKEN,
  "username": PIXELA_USERNAME,
  "agreeTermsOfService": "yes",
  "notMinor": "yes",
}

# pixelaResponse = requests.post(url=pixelaEndpoint, json=userParams)
# print(pixelaResponse.text)

# ---------- CREATING A GRAPH ---------- #
pixelaGraphEndpoint = f"{pixelaEndpoint}/{PIXELA_USERNAME}/graphs"

graphParams = {
  "id": GRAPH,
  "name": "Study Graph",
  "unit": "hr",
  "type": "float",
  "color": "sora",
}

headers = {
  "X-USER-TOKEN": PIXELA_TOKEN
}

# graphResponse = requests.post(url=pixelaGraphEndpoint, json=graphParams, headers=headers)
# print(graphResponse.text)

# ---------- POSTING PIXELS ---------- #
pixelPostEndpoint = f"{pixelaGraphEndpoint}/{GRAPH}"

pixelPostParams = {
  "date": formattedTodaysDate,
  "quantity": "1",
}

pixelPostResponse = requests.post(url=pixelPostEndpoint, json=pixelPostParams, headers=headers)

# ---------- UPDATING PIXELS ---------- #
pixelPutEndpoint = f"{pixelPostEndpoint}/20240105"

pixelPutParams = {
  "quantity": "1",
}

# pixelPutResponse = requests.put(url=pixelPutEndpoint, json=pixelPutParams, headers=headers)

# ---------- DELETING A PIXEL ---------- #
# pixelDeleteResponse = requests.delete(url=pixelPutEndpoint, headers=headers)