import requests
import json
from datetime import datetime

# Note: The code that actually interacts with the API is all commented out to not make any unintended actions
# Go through it in order, uncommenting when necessary, to make your own
# then the daily additions would be done within the "add" section
# API documentation found here: https://docs.pixe.la/

# Retrieve token and username from .gitignore'd json
with open('config.json', 'r') as data_file:
    config = json.load(data_file)
    username = config['pixela_username']
    token = config['pixela_token']

pixela_endpoint = 'https://pixe.la/v1/users'


# Use this to create user initially
user_params = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Uncomment ⬇ to create user
# create_user_response = requests.post(url=pixela_endpoint, json=user_params)
# print(create_user_response.text)


# Use this to create a graph initially
graph_endpoint = f'{pixela_endpoint}/{username}/graphs'

graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "hours",
    "type": "float",
    "color": "kuro"  # These are all using japanese color names, check pixela documentation for more options
}

headers = {
    "X-USER-TOKEN": token
}

# Uncomment ⬇ to create graph
# graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(graph_response.text)


# Adding pixel to graph
# This is the section that you would mostly be using if you want to add to pixela daily.
# some inputs can be added so the pixel_config data is asked for each time the script is run
add_pixel_endpoint = f'{pixela_endpoint}/{username}/graphs/{graph_config["id"]}'

today = datetime.now()  # or datetime(year=, month=, day=) for previous days

pixel_config = {
    'date': today.strftime('%Y%m%d'),  # formats it to pixela's needed format
    'quantity': '1.2'  # can use input() to fill this out daily
}

# Uncomment ⬇ to create pixel
# pixel_response = requests.post(url=add_pixel_endpoint, json=pixel_config, headers=headers)
# print(pixel_response.text)


# Updating a pixel
update_date = today.strftime("%Y%m%d")  # change date here in format yyyymmdd

update_pixel_endpoint = f'{pixela_endpoint}/{username}/graphs/{graph_config["id"]}/{update_date}'

update_pixel_config = {
    'quantity': '2.24'
}

# Uncomment ⬇ to update a pixel
# update_pixel_response = requests.put(url=update_pixel_endpoint, json=update_pixel_config, headers=headers)
# print(update_pixel_response.text)


# deleting a pixel
delete_date = today.strftime("%Y%m%d")  # change date here in format yyyymmdd

delete_pixel_endpoint = f'{pixela_endpoint}/{username}/graphs/{graph_config["id"]}/{delete_date}'

# Uncomment ⬇ to delete a pixel
# delete_pixel_response = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(delete_pixel_response.text)
