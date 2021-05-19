from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = r'C:\Users\rjl91\development\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('https://orteil.dashnet.org/cookieclicker/')

big_cookie = driver.find_element_by_id('bigCookie')

product_names = [f'product{i}' for i in range(17, -1, -1)]  # alternatively products = products[::-1]

products = [driver.find_element_by_id('name') for name in product_names]

for product in products:

# while True:
#     big_cookie.click()
#
#     product1 = driver.find_element_by_id('product1')
#     if product1.get_attribute('class') == 'product unlocked enabled':
#         product1.click()
#     product = driver.find_element_by_id('product0')
#     if product.get_attribute('class') == 'product unlocked enabled':
#         product.click()
#     try:
#         upgrade = driver.find_element_by_id('upgrade0')
#         if upgrade.get_attribute('class') == 'crate upgrade enabled':
#             upgrade.click()
#     except:
#         continue
