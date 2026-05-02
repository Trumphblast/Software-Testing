'''
 Here we login the website cange the screen sizes
'''

from selenium.webdriver.common.by import By
from selenium import webdriver
import time


url = "https://www.saucedemo.com/inventory.html"

driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

username = "standard_user"
password = "secret_sauce"

driver.find_element(By.ID, "user-name").send_keys(username)
driver.find_element(By.ID, "password").send_keys(password)
driver.find_element(By.NAME, "login-button").click()

viewPort = [(1800,645), (1494,1489), (233,583)]

for W , H in viewPort:
    driver.set_window_size(W , H)
    time.sleep(3)

driver.quit()
print(f"Successfully Done ")