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
    try:
        if city['lowestPrice'] > flight_data.price:
            print(f'{flight_data.destination_city} new deal is lower: {flight_data.price}')
            notification_manager.send_alert(flight_data)
    except AttributeError:
        pass  # can print an error message here if wanted - it comes up if there is nothing to compare with no flights
print('Done')
# The program does not always have an output, so may want to print more lines for debugging, but I commented them out
# for less clutter. At this stage, I thought just this one statement would be fine, but add back in if needed or wanted
