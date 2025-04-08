import requests
import os

parameters = {
    "lat": 31.520370,
    "lon": 74.358749,
    "appid": "c93513c092b531a2ff523fe4a8045f3d",
    "cnt": 4
}

bot_message = "Bring an Umbrella"
bot_token = os.environ.get("TELEGRAM_BOT_TOKEN")
bot_chatID = "6476086833"
api_key = os.environ.get("WEATHER_APPID")
print(f"API Key: {api_key}")
response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()

weather_data = response.json()

will_rain = False
for item in weather_data["list"]:
    condition_code = item["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    whatsapp_send = requests.get(send_text)
