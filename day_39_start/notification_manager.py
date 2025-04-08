import requests
import dotenv
import os

class NotificationManager:
    def __init__(self):
        dotenv.load_dotenv()
        self.bot_token = os.environ["BOT_API"]  # Replace with your Telegram bot token
        self.chat_id = os.environ["BOT_CHAT_ID"]      # Replace with your chat ID
        
    def send_message(self, message):
        telegram_api_url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"
        params = {
            "chat_id": self.chat_id,
            "text": message,
            "parse_mode": "HTML"  # Allows for basic HTML formatting
        }
        
        try:
            print(f"\nSending Telegram notification...")
            print(f"Message: {message}")
            response = requests.post(telegram_api_url, params=params)
            response.raise_for_status()
            print("Notification sent successfully!")
            return True
        except Exception as e:
            print(f"Error sending message: {e}")
            return False