import requests
import os
from dotenv import load_dotenv

data = [
  {
    "City": "Paris",
    "IATA Code": "CDG",
    "Lowest Price": 54
  },
  {
    "City": "Frankfurt",
    "IATA Code": "FRA",
    "Lowest Price": 42
  },
  {
    "City": "Tokyo",
    "IATA Code": "TYO",
    "Lowest Price": 485
  },
  {
    "City": "Hong Kong",
    "IATA Code": "HKG",
    "Lowest Price": 551
  },
  {
    "City": "Istanbul",
    "IATA Code": "IST",
    "Lowest Price": 95
  },
  {
    "City": "Kuala Lumpur",
    "IATA Code": "KUL",
    "Lowest Price": 414
  },
  {
    "City": "New York",
    "IATA Code": "NYC",
    "Lowest Price": 240
  },
  {
    "City": "San Francisco",
    "IATA Code": "SFO",
    "Lowest Price": 260
  },
  {
    "City": "Dublin",
    "IATA Code": "DUB",
    "Lowest Price": 378
  }
]


load_dotenv()

class DataManager:
    def __init__(self):
        self.sheety_api = os.environ["SHEETY_API"]
        self.end_point = "https://api.sheety.co/ef36e8925e3a54c57b07cb16957c6ac1/flightDeals/prices"
        self.send = None
        self.get_data()

    def get_data(self):
        response = requests.get(url=self.end_point, headers={"Authorization": self.sheety_api})
        if response.status_code == 200:
            data_from_sheet = response.json()["prices"]
            return data_from_sheet
        else:
            print(f"Error: {response.status_code}, {response.text}")

    def put_data(self, city_without_code):
        row_id = city_without_code["id"]
        body = {"price":
            {
            "city": city_without_code["city"],
            "iataCode": city_without_code["iataCode"],
            "lowestPrice": city_without_code["lowestPrice"]
                }
            }
        put_url = f"{self.end_point}/{row_id}"
        headers = {
            "Authorization": os.environ["SHEETY_API"],
            "Content-Type": "application/json"
        }
        self.send = requests.put(url=put_url, headers=headers, json=body)
        # Check if the request was successful
        if self.send.status_code == 200:
            print(self.send.json())
        else:
            print(f"Error: {self.send.status_code}, {self.send.text}")