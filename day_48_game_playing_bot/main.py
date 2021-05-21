"""
This code was designed for v 2.031 of the game and may not work on future
versions correctly.

Also, note that the cookies per second differs and is hardware based, so
performance changes when using different machines leaving benchmark comparisons
as unreliable metrics when sharing code.
"""


from selenium import webdriver
import time

# Create driver and get
chrome_driver_path = r'C:\Users\rjl91\development\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get('https://orteil.dashnet.org/cookieclicker/')

# Clicks accept cookies banner
time.sleep(3)
driver.find_element_by_css_selector('a.cc_btn_accept_all').click()

# Get elements
big_cookie = driver.find_element_by_id('bigCookie')

# Adding too many elements slows the clicking significantly, revert to range(17, -1, -1) for all products
# Decreasing the number of products to check improved my clicks from about 7-8 times per second
# to 18-19 per second
product_names = [f'product{i}' for i in range(3, -1, -1)]  # alternatively products = products[::-1]
product_elements = [driver.find_element_by_id(name) for name in product_names]

# Create a timers to check for upgrades and for stopping the game
upgrade_time = time.time() + 7
time_stop = time.time() + 300

# Running the game
while time.time() < time_stop:
    big_cookie.click()

    if time.time() < upgrade_time:
        # Buy upgrades
        try:
            upgrade = driver.find_element_by_id('upgrade0')
            if upgrade.get_attribute('class') == 'crate upgrade enabled':  # checks to see if purchasable
                upgrade.click()
        except:  # I don't like the bare except, but can't seem to get the error message to trigger the except otherwise
            pass  # Continue stops the loop totally, but pass just moves on to the next section

        # Buy products
        for product in product_elements:
            if product.get_attribute('class') == 'product unlocked enabled':  # checks to see if purchasable
                product.click()

        # Reset upgrade_time
        upgrade_time = time.time() + 7

# Output the number of cookies per second achieved
cps = driver.find_element_by_xpath('//*[@id="cookies"]')
print(cps.text)

driver.close()
