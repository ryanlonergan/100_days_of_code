import json
from selenium import webdriver
import time

# Set up link on search link for Linkedin
# I kept it like this so the arguments can be changed to inputs, but did not want to add the extra steps for testing
role = 'data scientist'  # input the role to search for
location = 'Seattle, Washington, United States'  # input the location in this format

role = role.replace(' ', '%20')  # strings are immutable, so no good way to do an in-place change
location = location.replace(' ', '%20').replace(',', '%2C')
url = f'https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=104116203&keywords={role}&location={location}&' \
      f'sortBy=R&redirect=false&position=1&pageNum=0'

# create driver
chrome_driver_path = r'C:\Users\rjl91\development\chromedriver.exe' # change to your local path
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url)

# Retrieve token and username from .gitignore'd json
with open('config.json', 'r') as data_file:
    config = json.load(data_file)
    linkedin_email = config['linkedin_email']
    linkedin_password = config['linkedin_password']

# handle login
time.sleep(2)
driver.find_element_by_css_selector('a.cta-modal__primary-btn').click()
time.sleep(2)
driver.find_element_by_id('username').send_keys(linkedin_email)
driver.find_element_by_id('password').send_keys(linkedin_password)
driver.find_element_by_xpath('//button[.="Sign in"]').click()

# todo find jobs


# todo apply or something