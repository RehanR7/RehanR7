import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 31.520370
MY_LONG = 74.358749
OFFSET_FOR_LAHORE = 5
MY_EMAIL = "rhnather@gmail.com"
TO_EMAIL = "rehan_biotech@yahoo.com"
PASSWORD = "qsyz cnds jndl eqgv"
HOST = "smtp.gmail.com"

def utc_to_local(utc_time, offset_time):
    local_time = (utc_time + offset_time) % 24
    return local_time

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if -5 <= iss_latitude - MY_LAT <= 5 and -5 <= iss_longitude - MY_LONG <= 5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    local_sunrise = utc_to_local(sunrise, OFFSET_FOR_LAHORE)
    local_sunset = utc_to_local(sunset, OFFSET_FOR_LAHORE)

    time_now = datetime.now()
    hour = time_now.hour

    if local_sunrise <= hour <= local_sunset:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP(HOST) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=TO_EMAIL,
                msg="Subject: ISS Overhead\n\nISS is near you. It can be seen today."
            )