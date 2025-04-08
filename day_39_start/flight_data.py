import requests
import datetime
from flight_search import FlightSearch
from notification_manager import NotificationManager


fs = FlightSearch()

class FlightData:
    def __init__(self):
        self.tomorrow = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime(format=f'%Y-%m-%d')
        self.six_months_from_now = (datetime.datetime.now() + datetime.timedelta(days=30 * 6)).strftime(format=f'%Y-%m-%d')
        self.total_prices = []
        self.flight_data = []  # Store flight data along with prices
        self.cheapest_overall = {
            "price": float('inf'),
            "from": "",
            "to": "",
            "departure": "",
            "arrival": "",
            "airline": ""
        }

    def search_for_flight(self, city_data):
        try:
            end_point = "https://test.api.amadeus.com/v2/shopping/flight-offers"
            header = {
                "Content-Type": "application/vnd.amadeus+json",
                "Authorization": f"Bearer {fs.get_new_token()}"
            }
            query = {
                "originLocationCode": "LON",
                "destinationLocationCode": city_data,
                "departureDate": self.tomorrow, 
                "returnDate": self.six_months_from_now,
                "adults": 1,
                "currencyCode": "GBP"
            }
            print(f"\nSearching flights for route LON-{city_data}")
            print(f"Dates: {self.tomorrow} to {self.six_months_from_now}")
            response = requests.get(url=end_point, headers=header, params=query)
            response.raise_for_status()
            data = response.json()
            if not data.get('data'):
                print(f"No flights found for {city_data}")
                if 'errors' in data:
                    print(f"API Error: {data['errors']}")
                return {"data": []}
            print(f"Found {len(data['data'])} flights")
            return data
        except requests.exceptions.RequestException as e:
            print(f"Error making API request for {city_data}: {e}")
            return {"data": []}

    def cheapest_flight(self, search_data, city_data):
        try:
            flights = search_data.get("data", [])
            if not flights:  # Handle empty list case
                return "N/A"
            
            lowest_price = float(flights[0]["price"]["grandTotal"])
            flight_info = {
                "price": lowest_price,
                "from": "LON",
                "to": city_data,
                "departure": flights[0]["itineraries"][0]["segments"][0]["departure"]["at"],
                "arrival": flights[0]["itineraries"][0]["segments"][-1]["arrival"]["at"],
                "airline": flights[0]["validatingAirlineCodes"][0]
            }
            
            for flight in flights:
                price = float(flight["price"]["grandTotal"])
                if price < lowest_price:
                    lowest_price = price
                    flight_info.update({
                        "price": price,
                        "departure": flight["itineraries"][0]["segments"][0]["departure"]["at"],
                        "arrival": flight["itineraries"][0]["segments"][-1]["arrival"]["at"],
                        "airline": flight["validatingAirlineCodes"][0]
                    })
            
            self.flight_data.append(flight_info)
            return lowest_price
        except (KeyError, ValueError, TypeError) as e:
            print(f"Error processing flight data for flight: {e}")
            return "N/A"
    
    def compare_prices(self, sheet_data):
        """Compare flight prices with sheet data and send notifications for better deals"""
        print("\nComparing prices with sheet data...")
        for flight in self.flight_data:
            # Find matching destination in sheet data
            for city_data in sheet_data:
                if city_data["IATA Code"] == flight["to"]:
                    sheet_price = float(city_data["Lowest Price"])
                    current_price = float(flight["price"])
                    print(f"Comparing {flight['to']}: Current £{current_price:.2f} vs Sheet £{sheet_price:.2f}")
                    
                    # If current price is lower than recorded lowest price
                    if current_price < sheet_price:
                        print(f"Found better deal for {flight['to']}!")
                        # Format the message as per the example
                        message = f"Low price alert! Only £{current_price:.2f} to fly\nfrom LHR to {flight['to']}, on {flight['departure'][:10]}\nuntil {flight['arrival'][:10]}."
                        
                        # Send notification
                        notification_manager = NotificationManager()
                        notification_manager.send_message(message)
