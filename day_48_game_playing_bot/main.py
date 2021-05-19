from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = r'C:\Users\rjl91\development\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('https://orteil.dashnet.org/cookieclicker/')