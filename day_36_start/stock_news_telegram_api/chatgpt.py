import requests


def stock_api():
    """
    Fetches stock data from Alphavantage API and returns:
    - stock_info: formatted stock price change info
    - first_date: the most recent trading date
    - second_date: the previous trading date
    """
    stock_symbol = "NVDA"
    stock_url = "https://www.alphavantage.co/query"
    stock_params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": stock_symbol,
        "apikey": "B5W2MTAK81QIJBVI"
    }

    try:
        response = requests.get(url=stock_url, params=stock_params)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching stock data: {e}")
        return None, None, None

    stock_data = response.json()

    # Check for expected data structure
    time_series = stock_data.get("Time Series (Daily)")
    if not time_series:
        print("Unexpected response format from stock API.")
        return None, None, None

    dates = list(time_series.keys())
    if len(dates) < 2:
        print("Not enough data available from stock API.")
        return None, None, None

    first_date = dates[0]
    second_date = dates[1]

    try:
        new_price = float(time_series[first_date]["4. close"])
        old_price = float(time_series[second_date]["4. close"])
    except (KeyError, ValueError) as e:
        print(f"Error processing stock data: {e}")
        return None, None, None

    percentage_change = ((new_price - old_price) / old_price) * 100
    percentage = round(percentage_change, 2)

    if percentage < 0:
        stock_info = f"{stock_symbol} 🔻 {percentage}%"
    else:
        stock_info = f"{stock_symbol} 🔺 {percentage}%"
    return stock_info, first_date, second_date


def news_api(from_date, to_date):
    """
    Fetches news related to NVIDIA from NewsAPI and returns a formatted headline and URL.
    """
    news_url = "https://newsapi.org/v2/everything"
    news_params = {
        "q": "NVIDIA stock OR NVDA price OR GPU market OR semiconductor industry OR AI chip",
        "searchIn": "title,description,content",
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": 1,  # Only need the most recent article
        "from": from_date,
        "to": to_date,
    }
    headers = {
        "Authorization": "752bfd03e784465f9202f2dfb569fff0"
    }

    try:
        response = requests.get(url=news_url, params=news_params, headers=headers)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching news data: {e}")
        return "News data not available."

    data = response.json()
    articles = data.get("articles")
    if not articles:
        return "No news articles found."

    try:
        headline = articles[0]["title"]
        article_url = articles[0]["url"]
    except KeyError as e:
        print(f"Error processing news data: {e}")
        return "News data not available."

    news_info = f"Headline: {headline}\nBrief: {article_url}"
    return news_info


def main():
    stock_info, first_date, second_date = stock_api()
    if not all([stock_info, first_date, second_date]):
        print("Failed to fetch stock data. Exiting.")
        return

    news_info = news_api(second_date, first_date)
    message = f"{stock_info}\n{news_info}"

    # Prepare Telegram message payload
    bot_chatID = "6476086833"
    bot_apikey = "7926954235:AAEWRzsos5bxF15c7o8WDcOtRmRQuyF2GYQ"
    telegram_url = f"https://api.telegram.org/bot{bot_apikey}/sendMessage"
    payload = {"chat_id": bot_chatID, "text": message}

    print("Payload to send:", payload)
    try:
        telegram_response = requests.post(telegram_url, json=payload)
        telegram_response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error sending message via Telegram: {e}")
        return
    print("Message sent successfully.")


if __name__ == "__main__":
    main()
