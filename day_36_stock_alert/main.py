import requests
import json
from twilio.rest import Client

# Change to whatever company you want info for
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# Get keys from a .gitignore'd config file
with open('config.json', 'r') as data_file:
    config = json.load(data_file)
    twilio_account_sid = config['twilio_account_sid']
    twilio_auth_token = config['twilio_auth_token']
    twilio_phone_number = config['twilio_phone_number']
    my_phone_number = config['my_phone_number']
    alpha_vantage_api_key = config['alpha_vantage_api_key']
    newsapi_api_key = config['newsapi_api_key']

# Retrieve stock information from Alpha Vantage api
stock_params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'outputsize': 'compact',
    'datatype': 'json',
    'apikey': alpha_vantage_api_key
}

stock_response = requests.get('https://www.alphavantage.co/query?', params=stock_params)
stock_response.raise_for_status()

# Processing returned data
stock_data = stock_response.json()
two_days = list(stock_data['Time Series (Daily)'].items())[:2]
day_1_close, day_2_close = float(two_days[0][1]['4. close']), float(two_days[1][1]['4. close'])
price_change = day_1_close/day_2_close - 1

# Sending text alert if condition is met
if abs(price_change) >= 0.001:  # Change delta to whatever value you want, like 0.05, left it very low to test

    # Retrieve articles for company from NewsAPI
    news_params = {
        'qInTitle': COMPANY_NAME,
        'apikey': newsapi_api_key
    }

    news_response = requests.get('https://newsapi.org/v2/everything?', params=news_params)
    news_response.raise_for_status()

    news_data = news_response.json()
    # Making sure there are enough articles to send
    if len(news_data['articles']) > 3:
        recent_news_data = news_data['articles'][:3]
    else:
        recent_news_data = news_data['articles']

    # Format price_change variable
    if price_change >= 0:
        price_percentage = f'🔺{round(price_change*100,1)}%'
    else:
        price_percentage = f'🔻{round(abs(price_change) * 100, 1)}%'

    msg_list = []  # Thought about using list comprehension here, but the f-string would make it hard to read
    for article in recent_news_data:
        msg_list.append(f'{STOCK} {price_percentage}\nHeadline: {article["title"]}\nBrief: {article["description"]}')

    # Comes down to personal opinion, but I think the for loop is somewhat easier to read than the list comprehension
    # They are more or less the same though, so use whichever one you prefer
    # msg_list = [f'{STOCK} {price_percentage}\nHeadline: {article["title"]}\nBrief: {article["description"]}'
    #             for article in recent_news_data]

    # Send a text for each article
    client = Client(twilio_account_sid, twilio_auth_token)
    for item in msg_list:
        message = client.messages \
            .create(
                body=item,
                from_=twilio_phone_number,
                to=my_phone_number
            )
        print(message.status)
