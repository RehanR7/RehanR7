import os
import requests
from dotenv import load_dotenv

load_dotenv()

class FlightSearch:
    def __init__(self):
        self.API_KEY = os.environ["AMADEUS_API_KEY"]
        self.API_SECRET = os.environ["AMADEUS_API_SECRET"]
        self.get_new_token()

    def get_new_token(self):
        end_point_access_token = "https://test.api.amadeus.com/v1/security/oauth2/token"
        head = {"Content-Type": "application/x-www-form-urlencoded"}
        parameters = {
            "grant_type": "client_credentials",
            "client_id": self.API_KEY,
            "client_secret": self.API_SECRET
        }
        response = requests.post(url=end_point_access_token, data=parameters, headers=head)
        response.raise_for_status()
        access_token = response.json()["access_token"]
        return access_token

    def iata_code_search(self, city_name):
        end_point = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
        header = {"Authorization": f"Bearer {self.get_new_token()}"}
        query = {
        "keyword": city_name,
        "max": "2",
        "include": "AIRPORTS"
        }
        response = requests.get(url=end_point,
                                params=query,
                                headers= header)
        print(f"Status code {response.status_code}. Airport IATA: {response.text}")
        try:
            code = response.json()["data"][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {city_name}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}.")
            return "Not Found"

        return code




