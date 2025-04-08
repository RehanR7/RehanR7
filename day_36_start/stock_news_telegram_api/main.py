import requests

STOCK_NAME = "NVDA"
STOCK_API = "B5W2MTAK81QIJBVI"

NEWS_API ="752bfd03e784465f9202f2dfb569fff0"

BOT_CHAT_ID = "6476086833"
BOT_API = "7926954235:AAEWRzsos5bxF15c7o8WDcOtRmRQuyF2GYQ"

YESTERDAY = ""
DAY_BEFORE_YESTERDAY = ""

def stock_api():
    global YESTERDAY, DAY_BEFORE_YESTERDAY
    stock_url = "https://www.alphavantage.co/query"
    stock_parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK_NAME,
        "apikey": STOCK_API
    }

    stock_response = requests.get(url=stock_url, params=stock_parameters)
    stock_response.raise_for_status()

    stock_data = stock_response.json()["Time Series (Daily)"]
    first_two_dates = list(stock_data.keys())[:2]
    YESTERDAY, DAY_BEFORE_YESTERDAY = first_two_dates
    new_price = float(stock_data[YESTERDAY]["4. close"])
    old_price = float(stock_data[DAY_BEFORE_YESTERDAY]["4. close"])
    difference = ((new_price - old_price) / old_price) * 100
    percentage = round(difference, 2)
    if percentage < 0:
        return f"{STOCK_NAME} 🔻 {abs(percentage)}% "
    else:
        return f"{STOCK_NAME} 🔺 {percentage}% "

def news_api():
    news_url = "https://newsapi.org/v2/everything"
    query_params = {
        "apiKey": NEWS_API,
        "qInTitle": "NVIDIA OR NVDA",
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": 3,
        "from": DAY_BEFORE_YESTERDAY,
        "to": YESTERDAY,
    }
    news_response = requests.get(url=news_url,
                                 params=query_params)
    news_response.raise_for_status()
    article_list = news_response.json()["articles"]
    return article_list

stock_info = stock_api()
articles = news_api()

for article in articles:
    url = f"https://api.telegram.org/bot{BOT_API}/sendMessage"
    payload = {"chat_id": BOT_CHAT_ID, "text": f"{stock_info}\n{article["url"]}"}
    print(payload)
    requests.post(url, json=payload)