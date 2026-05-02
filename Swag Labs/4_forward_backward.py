'''
  Here we do forward backward button and total links
  click menu -> click about -> backward -> forward -> refresh -> total links
'''


from selenium.webdriver.common.by import By
from selenium import webdriver
import time

url = "https://www.saucedemo.com/"

driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

username = "standard_user"
password = "secret_sauce"

driver.find_element(By.ID, "user-name").send_keys(username)
driver.find_element(By.ID, "password").send_keys(password)

# FIXED ❗ correct locator for login button
driver.find_element(By.ID, "login-button").click()

time.sleep(10)

# open left menu
driver.find_element(By.ID, "react-burger-menu-btn").click()
time.sleep(3)

# click About link
driver.find_element(By.ID, "about_sidebar_link").click()

# go back
driver.back()
time.sleep(3)

# refresh
driver.refresh()
time.sleep(3)

# go forward
driver.forward()

links = driver.find_elements(By.TAG_NAME, "a")
print(f"total links :{len(links)} ")

driver.close()
