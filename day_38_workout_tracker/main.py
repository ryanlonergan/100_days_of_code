import requests
import json
from datetime import datetime

# Retrieve token and username from .gitignore'd json
with open('config.json', 'r') as data_file:
    config = json.load(data_file)
    nutritionix_app_id = config['nutritionix_app_id']
    nutritionix_api_key = config['nutritionix_api_key']
    sheety_endpoint = config['sheety_endpoint']
    sheety_bearer_token = config['sheety_bearer_token']


# Ask user for what type of exercise they did in natural language, i.e. I swam for 20 minutes and ran 3 miles
exercise_text = input("What exercise did you do? ")

params = {
    'query': exercise_text  # can add gender, weight_kg, height_cm, age if wanted, more accurate if added
    # 'gender': string,
    # 'weight_kg': float,
    # 'height_cm': float,
    # 'age': int
}

# Send query to Nutritionx
nutritionx_url = 'https://trackapi.nutritionix.com/v2/natural/exercise'

headers = {
    "x-app-id": nutritionix_app_id,
    "x-app-key": nutritionix_api_key,
}

nutritionx_response = requests.post(nutritionx_url, headers=headers, json=params)
nutritionx_response.raise_for_status()
data = nutritionx_response.json()

# Record data that Nutritionx provides
sheety_header = {
    'Authorization': f'Bearer {sheety_bearer_token}'
}

for exercise in data['exercises']:
    sheety_details = {
        'workout': {
            'date': datetime.now().strftime('%m/%d/%Y'),
            'time': datetime.now().strftime('%X'),
            'exercise': exercise['name'].title(),
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories']
        }
    }

    sheety_response = requests.post(sheety_endpoint, headers=sheety_header, json=sheety_details)
    sheety_response.raise_for_status()
    print(sheety_response.text)
