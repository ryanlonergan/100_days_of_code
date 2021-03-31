import json
from twilio.rest import Client


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.

    def __init__(self):
        with open('config.json', 'r') as data_file:
            config = json.load(data_file)
            twilio_account_sid = config['twilio_account_sid']
            twilio_auth_token = config['twilio_auth_token']
            self.twilio_phone_number = config['twilio_phone_number']
            self.my_phone_number = config['my_phone_number']

        self.client = Client(twilio_account_sid, twilio_auth_token)

    def send_alert(self, flight_data):
        msg = f'Low price alert! Only ${flight_data.price} to fly from {flight_data.origin_city}-' \
              f'{flight_data.origin_airport} to {flight_data.destination_city}-{flight_data.destination_airport}, ' \
              f'from {flight_data.out_date} to {flight_data.return_date}'

        message = self.client.messages\
            .create(body=msg, from_=self.twilio_phone_number, to=self.my_phone_number)
        print(message.sid)  # prints out if message sends successfully
