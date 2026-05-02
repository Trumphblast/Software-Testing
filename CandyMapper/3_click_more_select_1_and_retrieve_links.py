'''
 We click on more option and retrieve links from that particular tab
'''

from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://candymapper.com/")

driver.find_element(By.ID, "popup-widget183-cta").click()
time.sleep(5)

driver.find_element(By.CSS_SELECTOR, "a[id='2']").click()
time.sleep(2)

driver.find_element(By.XPATH, "//a[@class='x-el x-el-a c1-58 c1-59 c1-34 c1-18 c1-19 c1-1l c1-s c1-64 c1-65 c1-1a c1-b c1-4c c1-1f c1-27 c1-5b c1-5c c1-5d c1-1g c1-1h c1-1i c1-1j'][normalize-space()='An Automation Sandbox?']").click()

links = driver.find_elements(By.TAG_NAME, "a")
print("Total Links : ", len(links))

for link in links:
    print(f"{link.text} -> {link.get_attribute('href')}")

