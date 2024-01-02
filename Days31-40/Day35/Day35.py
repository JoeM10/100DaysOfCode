import requests

apiKey = "07bf47c15077d70be69807ea65ae5578"
lattitude = 46.169519616665475
longitude = -123.01008783900251

apiEndPoint = f"https://api.openweathermap.org/data/2.5/forecast"

weatherParams = {
  "lat": lattitude,
  "lon": longitude,
  "units": "imperial",
  "appid": apiKey,
  "cnt": 4,
}

apiResponse = requests.get(apiEndPoint, params=weatherParams)
apiResponse.raise_for_status()
apiData = apiResponse.json()

forecast = [int(hourData["weather"][0]["id"]) for hourData in apiData["list"]]
willRain = False

for weather in forecast:
  if weather < 700:
    willRain = True

if willRain == True:
  print("Bring a umbrella!")