import requests
import datetime as dt

# split method sunset = data["sunset"].split("T")[1].split("+")[0]
# response = requests.get("http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
#
# latitude = data["iss_position"]["latitude"]
# longitude = data["iss_position"]["longitude"]
#
# iss_position = (latitude, longitude)
# print(iss_position)

LATITUDE = 31.520370
LONGITUDE = 74.358749
OFFSET_FOR_LAHORE = 5
parameters = {
    "lat": LATITUDE,
    "lng": LONGITUDE,
    "formatted": 0
}

def utc_to_local(utc_time, offset):
    local_hour = (utc_time + offset) % 24
    return local_hour

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()["results"]
print(data)
sunrise = int(data["sunrise"].split("T")[1].split(":")[0])
local_sunrise = utc_to_local(utc_time=sunrise, offset=OFFSET_FOR_LAHORE)
sunset = int(data["sunset"].split("T")[1].split(":")[0])
local_sunset = utc_to_local(utc_time=sunset, offset=OFFSET_FOR_LAHORE)

print(local_sunrise)

date = dt.datetime.now()
hour = date.hour
print(hour)