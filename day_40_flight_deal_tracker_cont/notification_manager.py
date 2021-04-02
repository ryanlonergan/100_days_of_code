import json
from twilio.rest import Client
import smtplib


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.

    def __init__(self):
        with open('config.json', 'r') as data_file:
            config = json.load(data_file)
            twilio_account_sid = config['twilio_account_sid']
            twilio_auth_token = config['twilio_auth_token']
            self.twilio_phone_number = config['twilio_phone_number']
            self.my_phone_number = config['my_phone_number']
            self.my_email = config['my_email']
            self.email_password = config['email_password']

        self.client = Client(twilio_account_sid, twilio_auth_token)

    def send_alert(self, msg):
        message = self.client.messages\
            .create(body=msg, from_=self.twilio_phone_number, to=self.my_phone_number)
        print(message.sid)  # prints out if message sends successfully

    def send_emails(self, emails, msg):
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user=self.my_email, password=self.email_password)
            for email in emails:
                connection.sendmail(from_addr=self.my_email,
                                    to_addrs=email,
                                    msg=f'Subject: New Low Price Flight!\n\n{msg}'.encode('utf-8'))
