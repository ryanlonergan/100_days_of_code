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
# personal LinkedIn account. To still get the experience of using Selenium, I elected to get the second item from the
# list of jobs, save it and then immediately unsave the job while finding and printing the role and position to the
# console as a compromise.
# todo find jobs
listings = driver.find_elements_by_css_selector('ul.jobs-search-results__list li')


for listing in listings:
    print(listing.text.splitlines())  # weird results


# ul
# class="jobs-search-results__list list-style-none"
# /html/body/div[5]/div[3]/div[3]/div/div/section[1]/div/div/ul
#
#
# //*[@id="ember930"]
# <a data-control-id="exJmZqgtImswwQwJZvra0A==" tabindex="0" href="/jobs/view/2581799886/?eBP=CwEAAAF51NvJrGghpWSHgF_y7hX6FjhDpNg73Tu14K64wvi6d_9TnNWTobwCHAKqCgiVCTTzaVf7SsVqFPqsHhPLdTIMeeAPENynlcGlAQySeRHgqkxfL3UeoqLBGMLj89fWXtuWIR0DzJl3fIYcaogBPHY4GAjREM3Cw53Uo-NpWmEScItGij7qvCdCzE2ivdX59DusiKs_Mk81weCgWznweC6NBRAoq2W_3V7Z6cX0lXXXQZBjATlgCVscSgVCJkcsLY8O2CRYleU5X1DO5y4tDng34Ufb_E97fNP8uCzMuEJrujWYQh7GXhZ4E0NIH-dZXhUbzc-x0OO28LQAlvGRuJ4GrJwu&amp;refId=%2F%2BbBlAAF8jXjl6Fnet%2FihQ%3D%3D&amp;trackingId=exJmZqgtImswwQwJZvra0A%3D%3D&amp;trk=flagship3_search_srp_jobs" id="ember937" class="disabled ember-view job-card-container__link job-card-list__title">
#             Data Analyst
#           </a>
# //*[@id="ember938"]/div
# <div class="job-card-container__company-name">
#               Parker &amp; Lynch
#             </div>
# todo apply or something
