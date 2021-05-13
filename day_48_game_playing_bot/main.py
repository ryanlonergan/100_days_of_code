from selenium import webdriver

chrome_driver_path = r'C:\Users\rjl91\development\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# testing Selenium - redo of day 47
driver.get('https://www.amazon.com/Instant-Pot-Plus-Programmable-Sterilizer/dp/B08PQ2KWHS?ref_=ast_sto_dp&th=1')
price = driver.find_element_by_id('priceblock_ourprice')
print(price.text)

# driver.close()  # close tab
driver.quit()  # quit window
