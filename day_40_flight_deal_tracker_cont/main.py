from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from datetime import datetime, timedelta

# Customizable Variables
# Change this variable to your local airport
fly_from = 'SEA'

# Change the timedelta's to be in the range you want
date_from = (datetime.now() + timedelta(days=1)).strftime('%d/%m/%Y')  # starting date, currently set to tomorrow
date_to = (datetime.now() + timedelta(days=180)).strftime('%d/%m/%Y')  # end date, currently set to 6 months from today


flight_search = FlightSearch()
data_manager = DataManager()
notification_manager = NotificationManager()

sheet_data = data_manager.retrieve_data(False)  # Change to True to use an API call - only 200 a month though
data_manager.update_destination_code(sheet_data)

for city in sheet_data:
    fly_to = city['iataCode']
    flight_data = flight_search.check_flights(fly_from, fly_to, date_from, date_to)

    if flight_data is None:
        continue

    if flight_data.price < city['lowestPrice']:
        msg = f'Low price alert! Only ${flight_data.price} to fly from {flight_data.origin_city}-' \
              f'{flight_data.origin_airport} to {flight_data.destination_city}-{flight_data.destination_airport}, ' \
              f'from {flight_data.out_date} to {flight_data.return_date}'

        # add extra line if there is a stop over
        if flight_data.stop_overs > 0:
            msg += f"\nFlight has {flight_data.stop_overs} stop over, via {flight_data.via_city}."

        flight_link = f'https://www.google.com/flights?hl=en#flt={flight_data.origin_airport}.' \
                      f'{flight_data.destination_airport}.{flight_data.out_date}*{flight_data.destination_airport}.' \
                      f'{flight_data.origin_airport}.{flight_data.return_date}'
        msg += f'\n{flight_link}'

        users = data_manager.get_customer_emails()
        emails = [row["email"] for row in users]

        notification_manager.send_emails(emails, msg)
        # notification_manager.send_alert(msg)  # Uncomment to send texts
print('Done')
