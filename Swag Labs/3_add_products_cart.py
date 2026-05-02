'''
  Here we have chain of automation of ordering the item
  login -> add products -> click basket -> add details -> print details in compiler -> finsih
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

time.sleep(3)

products = ["add-to-cart-sauce-labs-backpack", "add-to-cart-sauce-labs-fleece-jacket", "add-to-cart-sauce-labs-onesie"]

for product in products:
    time.sleep(3)
    driver.find_element(By.ID, product).click()
    time.sleep(3)

driver.find_element(By.ID, "shopping_cart_container").click()
time.sleep(10)
verify_cart = driver.find_element(By.ID, "checkout").click()
time.sleep(3)
#verify_cart = verify_cart.text
#if verify_cart == "Checkout":

print("Hey! we added the 3 items to the cart")

#print("We did not add the 3 items to the cart")

driver.find_element(By.ID, "first-name").send_keys("Bharath")
driver.find_element(By.ID, "last-name").send_keys("Kumar")
driver.find_element(By.ID, "postal-code").send_keys("123456")
time.sleep(3)

ordered = driver.find_element(By.ID, "continue").click()

summary = driver.find_element(By.CLASS_NAME, "summary_info")
print()
print(summary.text)
time.sleep(3)
finish = driver.find_element(By.ID, "finish").click()
time.sleep(3)
success = driver.find_element(By.ID, "checkout_complete_container")
print()
print(success.text)
driver.quit()