import requests
import json


class DataManager:

    def __init__(self):
        with open('config.json', 'r') as data_file:
            config = json.load(data_file)
            self.sheety_endpoint = config['sheety_endpoint']
            self.sheety_users_endpoint = config['sheety_users_endpoint']
            self.sheety_bearer_token = config['sheety_bearer_token']

        self.sheety_header = {
            'Authorization': f'Bearer {self.sheety_bearer_token}'
        }

    def retrieve_data(self, call_sheety: bool = False) -> list:
        """
        A function that retrieves data from an API or stored list. Helps to limit API calls with sheety as it only
        offers 200 per month on the free tier

        :param call_sheety: Bool value for getting data from API, uses stored data when false
        :return: A list of dictionary values of cities, their city code for airports, lowest price for tickets and rowid
        """
        if call_sheety:
            sheety_response = requests.get(self.sheety_endpoint, headers=self.sheety_header)
            sheety_response.raise_for_status()
            data = sheety_response.json()["prices"]
        else:
            data = [{"city": "Paris", "iataCode": "PAR", "lowestPrice": 54, "id": 2},
                    {"city": "Berlin", "iataCode": "BER", "lowestPrice": 42, "id": 3},
                    {"city": "Tokyo", "iataCode": "TYO", "lowestPrice": 485, "id": 4},
                    {"city": "Sydney", "iataCode": "SYD", "lowestPrice": 551, "id": 5},
                    {"city": "Istanbul", "iataCode": "IST", "lowestPrice": 95, "id": 6},
                    {"city": "Kuala Lumpur", "iataCode": "KUL", "lowestPrice": 414, "id": 7},
                    {"city": "New York", "iataCode": "NYC", "lowestPrice": 240, "id": 8},
                    {"city": "San Francisco", "iataCode": "SFO", "lowestPrice": 260, "id": 9},
                    {"city": "Cape Town", "iataCode": "CPT", "lowestPrice": 378, "id": 10},
                    {"city": "Nagoya", "iataCode": "NGO", "lowestPrice": 5001, "id": 11}]
        return data

    def update_destination_code(self, data):
        import flight_search

        flight_search = flight_search.FlightSearch()

        for city in data:
            if city['iataCode'] == '':
                update_endpoint = f'{self.sheety_endpoint}/{city["id"]}'
                update_data = {
                    'price': {
                        'iataCode': flight_search.get_destination_code(city['city'])
                    }
                }
                update_response = requests.put(update_endpoint, headers=self.sheety_header, json=update_data)
                update_response.raise_for_status()
                # print(update_response.text)  # Uncomment to see if it is working

    def get_customer_emails(self):
        customers_endpoint = self.sheety_users_endpoint
        response = requests.get(customers_endpoint, headers=self.sheety_header)
        data = response.json()
        customer_data = data["users"]
        return customer_data
