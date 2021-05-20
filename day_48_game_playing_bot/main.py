from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = r'C:\Users\rjl91\development\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('https://orteil.dashnet.org/cookieclicker/')

big_cookie = driver.find_element_by_id('bigCookie')

product_names = [f'product{i}' for i in range(17, -1, -1)]  # alternatively products = products[::-1]

# p0 = driver.find_element_by_xpath('//*[@id="product0"]')
# print(p0.text)


# for name in product_names:
#     drivers = driver.find_element_by_id('name')
#     print(drivers.text)
# products = [driver.find_element_by_id('name') for name in product_names]

# for product in products:
#     print(product)

while True:
    big_cookie.click()

    # Todo add in timer - do this every 5 seconds


    # todo move the product drivers to a list? maybe that would work better? - slows down because it the list each iteration, but never buys
    for name in product_names:
        product = driver.find_element_by_id(name)
        if product.get_attribute('class') == 'product unlocked enabled':
            product.click()
        # except AttributeError:
        #     print('uh oh')
        #     continue




    # product1 = driver.find_element_by_id('product1')
    # if product1.get_attribute('class') == 'product unlocked enabled':
    #     product1.click()
    # product = driver.find_element_by_id('product0')
    # if product.get_attribute('class') == 'product unlocked enabled':
    #     product.click()

    # Buy upgrades
    try:
        upgrade = driver.find_element_by_id('upgrade0')
        if upgrade.get_attribute('class') == 'crate upgrade enabled':
            upgrade.click()
    except:  # I don't like the bare except, but can't seem to get the error message to trigger the except otherwise
        continue

# todo annoying banner ad button - wait 3 seconds and click
# <a href="#null" data-cc-event="click:dismiss" target="_blank" class="cc_btn cc_btn_accept_all">Got it!</a>