"""
Checks a csv list of birthdays and sends a random pre-made letter to that person if it is their birthday
"""

import smtplib
import json
import datetime as dt
import csv
from random import randint, choice

# loads email from config file
# using this method and .gitignore to upload to public repo
with open('config.json', 'r') as data_file:
    config = json.load(data_file)

my_email = config['email']
password = config['password']

# getting birthdays
birthdays = []
with open('birthdays.csv', 'r') as data:
    for line in csv.DictReader(data):
        birthdays.append(line)

# Check to see if there are any birthdays today
now = dt.datetime.now()
for person in birthdays:
    if int(person['month']) == now.month and int(person['day']) == now.day:  # only runs if there is a birthday this day

        # Pick a random letter from available choices
        letter_filepath = f'./letter_templates/letter_{randint(1, 3)}.txt'

        # Getting default email text and replacing placeholder with their name
        with open(letter_filepath, 'r') as template:
            letter_template = template.read()
        complete_letter = letter_template.replace('[NAME]', person['name'])

        # Combining another project here and adding a random quote as a signature to each letter
        with open('quotes.txt', 'r') as quotes:
            lines = quotes.readlines()
            quote = choice(lines)
        complete_letter += '\n\n' + quote

        # Sending email
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=my_email,  # replace to_addrs with person['email']
                                msg=f'Subject:Happy Birthday, {person["name"]}!\n\n'
                                    f'{complete_letter}'.encode('utf-8'))
        print('Script finished')
