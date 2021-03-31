import requests
import json
from flight_data import FlightData


class FlightSearch:

    def __init__(self):
        with open('config.json', 'r') as data_file:
            config = json.load(data_file)
            self.tequila_api = config['tequila_api']

        self.tequila_header = {
            'apikey': self.tequila_api
        }

        self.tequila_dest_endpoint = 'https://tequila-api.kiwi.com/locations/query'
        self.tequila_flights_endpoint = 'https://tequila-api.kiwi.com/v2/search'

    def get_destination_code(self, city_name):
        search_data = {
            'term': city_name,
            'location_types': 'airport'
        }
        tequila_response = requests.get(self.tequila_dest_endpoint, headers=self.tequila_header, params=search_data)
        tequila_response.raise_for_status()
        location_data = tequila_response.json()
        code = location_data['locations'][0]['city']['code']
        return code

    def check_flights(self, fly_from, fly_to, date_from, date_to):
        check_data = {
            'fly_from': fly_from,
            'fly_to': fly_to,
            'date_from': date_from,
            'date_to': date_to,
            'nights_in_dst_from': 7,
            'nights_in_dst_to':  28,
            'flight_type': 'round',
            'one_for_city': 1,
            'curr': 'USD',
            'max_stopovers': 0
        }

        tequila_flights_response = requests.get(
            self.tequila_flights_endpoint,
            headers=self.tequila_header,
            params=check_data
        )
        # tequila_flights_response.raise_for_status()  # Creates extra errors as there are many missing flights w/ covid

        try:
            data = tequila_flights_response.json()['data'][0]
        except IndexError:
            # print(f"No flights found for {fly_to}.")  # Uncomment for testing - limited flights with covid
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        # print(f"{flight_data.destination_city}: ${flight_data.price}")  # uncomment for testing
        return flight_data
