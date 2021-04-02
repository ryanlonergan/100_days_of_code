import os
import requests

# Note: This page gets hosted on Replit and allows users to signup for flight deal alerts
# To get it to work on there, you need an .env file with the "SHEETY_ENDPOINT" and "SHEETY_BEARER_TOKEN"
# Replit will keep the .env only visible to you
sheety_endpoint = os.getenv("SHEETY_ENDPOINT")
sheety_bearer_token = os.getenv("SHEETY_BEARER_TOKEN")
sheety_header = {'Authorization': f'Bearer {sheety_bearer_token}'}

signup_successful = False

print('Weclome to Ryan\'s Flight Club.\nWe find the best deals and email you.')
first_name = str(input('What is your first name?\n'))
last_name = str(input('What is your last name?\n'))

while not signup_successful:
    email = str(input('What is your email?\n'))
    email_confirm = str(input('Please confirm your email:\n'))

    if email == email_confirm: # Very simple email verification, not meant for anything serious
        signup_successful = True
    else:
        print('Your emails did not match. Please try again.')

update_data = {
    'user': {
      'firstName': first_name,
      'lastName': last_name,
      'email': email
    }
  }

sheety_response = requests.post(sheety_endpoint, headers=sheety_header, json=update_data)
sheety_response.raise_for_status()
print('You\'re in the club!')
