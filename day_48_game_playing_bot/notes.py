from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = r'C:\Users\rjl91\development\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

#  # testing Selenium with amazon- alternate method of day 47
# driver.get('https://www.amazon.com/Instant-Pot-Plus-Programmable-Sterilizer/dp/B08PQ2KWHS?ref_=ast_sto_dp&th=1')
# price = driver.find_element_by_id('priceblock_ourprice')
# print(price.text)

#  # More examples with python.org site
# driver.get('https://www.python.org/')

# search_bar = driver.find_element_by_name('q')
# print(search_bar.get_attribute('placeholder'))

# logo = driver.find_element_by_class_name('python-logo')
# print(logo.size)

# documentation_link = driver.find_element_by_css_selector('.documentation-widget a')
# print(documentation_link.text)

# issues_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(issues_link.get_attribute('href'))

#  # Challenge - scrape upcoming events and put their date and name in a dict on python.org
# I prefer the second method as it doesn't create an extra list, but the difference is small

# event_dates = driver.find_elements_by_css_selector('.event-widget time')
# event_names = driver.find_elements_by_css_selector('.event-widget li a')
#
# event_dict = {i: {'time': event_dates[i].text, 'name': event_names[i].text} for i in range(len(event_dates))}
# print(event_dict)

# events = driver.find_elements_by_css_selector('.event-widget li')
#
# event_dict = {i: {'time': events[i].find_element_by_tag_name('time').text,
#                   'name': events[i].find_element_by_tag_name('a').text} for i in range(len(events))}
# print(event_dict)

###########

# Another challenge - click the total number of articles on wikipedia
# driver.get('https://en.wikipedia.org/wiki/Main_Page')
# article_count = driver.find_element_by_css_selector('#articlecount a')
# article_count.click()

# finding element by the link text
# all_portals = driver.find_element_by_link_text('All portals')
# all_portals.click()

# inputting a search
# search = driver.find_element_by_name('search')
# search.send_keys('Python')
# search.send_keys(Keys.ENTER)

#########
# Challenge - fill out the sign up on this (fake) website

driver.get('http://secure-retreat-92358.herokuapp.com/')
fname = driver.find_element_by_name('fName')
lname = driver.find_element_by_name('lName')
email = driver.find_element_by_name('email')
button = driver.find_element_by_css_selector('form button')

fname.send_keys('test')
lname.send_keys('test')
email.send_keys('test@test.com')
button.click()

# driver.close()  # close tab
# driver.quit()  # quit window
