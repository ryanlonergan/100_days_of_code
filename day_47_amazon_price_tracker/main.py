import json
import smtplib

import requests

from bs4 import BeautifulSoup
import lxml

# Change this url to whatever item you want to track and the price you want the alert to trigger at
url_to_track = 'https://www.amazon.com/Instant-Pot-Plus-Programmable-Sterilizer/dp/B08PQ2KWHS?ref_=ast_sto_dp&th=1'
buy_price = 200  # Leave this high for testing

# The headers may have to be changed to have Amazon not think you're a bot
# These headers worked for me, but you may have to alter it - Use http://myhttpheader.com/ to see your headers
request_headers = {'Accept-Encoding': 'gzip, deflate',
                   'Accept-Language': 'en-US,en;q=0.9',
                   'User-Agent': 'Defined'}

response = requests.get(url=url_to_track, headers=request_headers)
amazon_page = response.text

# Use BeautifulSoup to parse Amazon page
# Can try the html parser, but lxml provided better results for me
soup = BeautifulSoup(amazon_page, 'lxml')

try:
    # Get product price
    product_price_string = soup.find(name="span", id="priceblock_ourprice").text
    product_price = float(product_price_string.replace('$', '').replace(',', ''))  # Formatting price to float
    # print(product_price)  # Use for testing

    # Get product title
    product_title_string = soup.find(name="span", id="productTitle").text.strip()  # Remove extra blank lines
    # print(product_title_string)  # Use for testing

    # check if current price is lower than buy price and send an email alert if True
    if product_price < buy_price:

        # loads email address and password from config file
        # using this method and .gitignore to upload to public repo
        with open('config.json', 'r') as data_file:
            config = json.load(data_file)
            my_email = config['email']
            password = config['password']
            print(my_email, password)

        message = f'Subject: Amazon Price Alert\n\n' \
                  f'{product_title_string} is now ${product_price}. Check it out here:\n{url_to_track}'

        # sends message with SMTP - following is specific for gmail and changes may be needed for other email providers
        with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=my_email,
                                msg=message)

except AttributeError:
    # Prints a more helpful error message
    print('Amazon thinks you are a bot. Try changing your request headers.')
