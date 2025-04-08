import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()
# NUTRITION_IX_API

NUTRITION_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/ef36e8925e3a54c57b07cb16957c6ac1/workoutTracking/workouts"
QUERY = input("Tell me which exercises you did: ")

header = {
    "x-app-id": os.getenv("APPLICATION_ID"),
    "x-app-key": os.getenv("APPLICATION_KEY")
}
nutrition_params = {
    "query": QUERY,
    "gender": "male",
    "weight_kg": 50,
    "height_cm": 165,
    "age": 23
}

nut_response = requests.post(url=NUTRITION_ENDPOINT, json=nutrition_params, headers=header)
nut_response.raise_for_status()

data = nut_response.json()["exercises"][0]
DATE = datetime.now().strftime(format="%d/%m/%Y")
TIME = datetime.now().strftime(format="%X")

EXERCISE = data["user_input"]
DURATION = data["duration_min"]
CALORIES = data["nf_calories"]

sheety_params = {
    "workout":
        {
    "date": DATE,
    "time": TIME,
    "exercise": EXERCISE.title(),
    "duration": DURATION,
    "calories": CALORIES
        }
}
sheety_header = {"Authorization": os.getenv("SHEETY_API")}

response = requests.post(url=SHEETY_ENDPOINT, json=sheety_params, headers=sheety_header)
response.raise_for_status()