'''
 Here we open swag lab then create new tab open candymapper and take a screenshot

'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url1 = 'https://www.saucedemo.com/'
url2 = 'https://candymapper.com/'

driver = webdriver.Edge()

driver.get(url1)
driver.maximize_window()
time.sleep(3)
driver.switch_to.new_window()
driver.get(url2)
driver.save_screenshot("candymapper_screenshot.png")

time.sleep(3)

print("Opened Candy Mapper Website and taken screenshot")








