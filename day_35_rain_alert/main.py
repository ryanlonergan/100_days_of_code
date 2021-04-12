import requests
from twilio.rest import Client
import json

# Note on hiding api keys
# os.environ.get() didn't work within my PyCharm on Windows easily
# Might be an issue with windows and there may be a work around using dotenv package
# I decided to just use a config.json file to hide my keys and another option would be a .env file
with open('config.json', 'r') as data_file:
    config = json.load(data_file)
    owm_api_key = config['owm_api_key']
    twilio_account_sid = config['twilio_account_sid']
    twilio_auth_token = config['twilio_auth_token']
    twilio_phone_number = config['twilio_phone_number']
    my_phone_number = config['my_phone_number']

OWM_Endpoint = 'https://api.openweathermap.org/data/2.5/onecall'
parameters = {
    'lat': 47.760113,  # Edit this to your own latitude
    'lon': -122.205444,  # Edit this to your own longitude
    'exclude': 'current,minutely,daily',
    'appid': owm_api_key
}

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()

data = response.json()

# Condition to check to see if there is rain or other inclement weather
# Basically any code less than 700 is a type of rain or snow where you may want an umbrella
# Full info here: https://openweathermap.org/weather-conditions
if [True for weather_12hr in data['hourly'][:12] if weather_12hr['weather'][0]['id'] < 700]:
    client = Client(twilio_account_sid, twilio_auth_token)
    message = client.messages \
        .create(
            body="It's going to rain today. Remember to bring an ☔",
            from_=twilio_phone_number,
            to=my_phone_number
        )

    print(message.status)

# Upload this script to PythonAnywhere, AWS Lambda or another similar service and run it daily in the morning
# to get the alerts daily
