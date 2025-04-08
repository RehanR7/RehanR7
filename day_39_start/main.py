from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from data_manager import data
from notification_manager import NotificationManager

notification_manager = NotificationManager()
data_manager = DataManager()
flight_search = FlightSearch()
flight_data = FlightData()

# sheet_data = data_manager.get_data()
sheet_data = data

print("\nSearching for flights from London...\n")

for city in sheet_data:
    if city["IATA Code"] == "":
        city_name = city["City"]
        search_code = flight_search.iata_code_search(city_name)
        city["IATA Code"] = search_code
        data_manager.put_data(city)
    else:
        search_data = flight_data.search_for_flight(city_data=city["IATA Code"])
        lowest_price = flight_data.cheapest_flight(search_data, city["IATA Code"])
        flight_data.total_prices.append(lowest_price)
        print(f"Lowest price for {city['City']} ({city['IATA Code']}): £{lowest_price}")

# Find the cheapest flight from all destinations
if flight_data.flight_data:
    cheapest_flight = min(flight_data.flight_data, key=lambda x: float(x['price']) if x['price'] != 'N/A' else float('inf'))
    
    print("\n" + "="*50)
    print("CHEAPEST FLIGHT FOUND:")
    print(f"Route: {cheapest_flight['from']} → {cheapest_flight['to']}")
    print(f"Price: £{cheapest_flight['price']}")
    print(f"Airline: {cheapest_flight['airline']}")
    print(f"Departure: {cheapest_flight['departure']}")
    print(f"Arrival: {cheapest_flight['arrival']}")
else:
    print("\nNo valid flights found")

flight_data.compare_prices(sheet_data)

