import os
import requests
from datetime import datetime

# ---------- CONSTANTS ---------- #
NUTRITIONIX_API_KEY = os.environ.get("NUTRITIONIX_API_KEY")
NUTRITIONIX_APP_ID = os.environ.get("NUTRITIONIX_APP_ID")

SHEETY_API_KEY = os.environ.get("SHEETY_API_KEY")
SHEETY_USERNAME = os.environ.get("SHEETY_USERNAME")
SHEETY_PASSWORD = os.environ.get("SHEETY_PASSWORD")

WEIGHT_KG = 69
HEIGHT_CM = 175.26
AGE = 27

# ---------- VARIABLES ---------- #
todaysDate = datetime.now().strftime("%d/%m/%Y")
currentTime = datetime.now().strftime("%H:%M:%S")

exerciseQuestion = str(input("What exercise did you do: "))

# ---------- ENDPOINTS ---------- # 
nutritionixExerciseEndpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
nutritionixItemEndpoint = "https://trackapi.nutritionix.com/v2/search/item"
nutritionixInstantEndpoint = "https://trackapi.nutritionix.com/v2/search/instant"
nutritionixNutrientsEndpoint = "https://trackapi.nutritionix.com/v2/natural/nutrients"

sheetyEndpoint = f"https://api.sheety.co/{SHEETY_API_KEY}/myWorkoutsCodingProject/workouts"

# ---------- NUTRITIONIX DICTS ---------- #
nutritionixHeaders = {
  "x-app-id": NUTRITIONIX_APP_ID,
  "x-app-key": NUTRITIONIX_API_KEY,
}

nutritionixParams = {
  "query": exerciseQuestion,
  "weight_kg": WEIGHT_KG,
  "height_cm": HEIGHT_CM,
  "age": AGE
}

# ---------- NUTRITIONIX REQUESTS ---------- #
nutritionixExerciseResponse = requests.post(url=nutritionixExerciseEndpoint, json=nutritionixParams, headers=nutritionixHeaders)
nutritionixExerciseResponse.raise_for_status()
exerciseData = nutritionixExerciseResponse.json()

# ---------- SHEETY DICTS ---------- #
sheetyParams = {
  "workout": {
    "date": todaysDate,
    "time": currentTime,
    "exercise": exerciseData["exercises"][0]["name"].title(),
    "duration": float(exerciseData["exercises"][0]["duration_min"]),
    "calories": int(exerciseData["exercises"][0]["nf_calories"]),
  }
}

# ---------- SHEETY REQUESTS ---------- #
sheetyPostResponse = requests.post(url=sheetyEndpoint, json=sheetyParams, auth=(SHEETY_USERNAME, SHEETY_PASSWORD))
sheetyPostResponse.raise_for_status()