import json
from selenium import webdriver
import time

# Set up link on search link for Linkedin - change role and location to meet your needs
# I kept it like this so the arguments can be changed to inputs, but did not want to add the extra steps for testing
role = 'data scientist'  # input the role to search for
location = 'Seattle, Washington, United States'  # input the location in this format

role = role.replace(' ', '%20')  # strings are immutable, so no good way to do an in-place change
location = location.replace(' ', '%20').replace(',', '%2C')
url = f'https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=104116203&keywords={role}&location={location}&' \
      f'sortBy=R&redirect=false&position=1&pageNum=0'

# create driver
chrome_driver_path = r'C:\Users\rjl91\development\chromedriver.exe'  # change to your local path
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url)
driver.maximize_window()

# Retrieve token and username from .gitignore'd json
with open('config.json', 'r') as data_file:
    config = json.load(data_file)
    linkedin_email = config['linkedin_email']
    linkedin_password = config['linkedin_password']

# handle login
time.sleep(3)
driver.find_element_by_css_selector('a.cta-modal__primary-btn').click()
time.sleep(3)
driver.find_element_by_id('username').send_keys(linkedin_email)
driver.find_element_by_id('password').send_keys(linkedin_password)
driver.find_element_by_xpath('//button[.="Sign in"]').click()

# Note - the original intent of this project was to apply for jobs automatically, but I did not want to do that on my
# personal LinkedIn account. To still get the experience of using Selenium, I elected to get the list of jobs, print
# the roles and positions and then saving and immediately unsaving the first job as a compromise.

# Get the job listings and click through them while performing actions
listings = driver.find_elements_by_class_name('jobs-search-results__list-item')

for listing in listings:
    # Click on each listing
    listing.click()
    # Extract and print position and company to console
    position = driver.find_element_by_class_name('jobs-details-top-card__job-title').text
    company = driver.find_element_by_class_name('jobs-details-top-card__company-url').text
    print(f'Position: {position} Company: {company}')  # Cleaner to assign text to variables than to include in print

    # Save and unsave each job
    time.sleep(1)
    driver.find_element_by_css_selector('button.jobs-save-button').click()
    time.sleep(1)
    driver.find_element_by_css_selector('button.jobs-save-button').click()
    time.sleep(1)
    # I had originally used the following function to click the unsave button, but it does not work for the list
    # driver.find_element_by_xpath('//*[text()="Unsave"]').click()  # //button did not work, but wildcard did

    # Note - The sleep functions are very important as linkedin does not change the page immediately, but may not work
    # later on or on every computer
    # If you need to change the times for sleep, check the following page for any jobs it was unable to unsave
    # https://www.linkedin.com/my-items/saved-jobs/

# I ended up not needing to use any exceptions, but Selenium has its own which I wanted to make a note of
# from selenium.common.exceptions import NoSuchElementException
