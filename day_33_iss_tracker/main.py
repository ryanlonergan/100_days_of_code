import requests
import datetime as dt
import json
import smtplib
import time

# Adjust these to match your own values
MY_LAT = 47.760090
MY_LNG = -122.205429


# get ISS location and returns true if it is + or - 5 degrees overhead
def is_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    lat_diff = MY_LAT - iss_latitude
    lng_diff = MY_LNG - iss_longitude

    if (5 > lat_diff > -5) and (5 > lng_diff > -5):
        return True


# Determines your sunrise and sunset times to determine if it is dark enough to see the ISS
def is_dark():
    parameters = {
        'lat': MY_LAT,
        'lng': MY_LNG,
        'formatted': 0
    }

    response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
    response.raise_for_status()

    data = response.json()
    sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])

    # using dt.timezone should allow for the code to be run anywhere without the user having to enter their own offset
    time_now = dt.datetime.now(dt.timezone.utc).hour

    if sunrise >= time_now >= sunset:
        return True


# This will run the program constantly to check if the space station is overhead - alter the time to sleep as needed
while True:
    time.sleep(60)
    if is_overhead():
        if is_dark():
            # loads email address and password from config file
            # using this method and .gitignore to upload to public repo
            with open('config.json', 'r') as data_file:
                config = json.load(data_file)
                my_email = config['email']
                password = config['password']

            message = 'Subject:You Should Look Up\n\n The International Space Station is overhead and you ' \
                      'should be able to see it in the night sky!'

            with smtplib.SMTP('smtp.gmail.com', 587) as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email,
                                    to_addrs=my_email,
                                    msg=message)
        else:
            print('The ISS is overhead, but it is not dark.')
    else:
        print('The ISS is not overhead')  # left in these print statements for troubleshooting, otherwise no output
