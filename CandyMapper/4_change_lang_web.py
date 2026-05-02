'''
 here we change the lang of the website
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

url = "https://candymapper.com/"

driver = webdriver.Edge()
driver.maximize_window()
driver.get(url)

driver.find_element(By.ID, "popup-widget183-cta").click()
time.sleep(5)

driver.find_element(By.XPATH, "//div[@class='x-el x-el-div c1-1 c1-2 c1-o c1-b c1-c c1-d c1-p c1-e c1-f c1-g']//div[@class='x-el x-el-div i18n-icon c1-1 c1-2 c1-q c1-r c1-s c1-t c1-u c1-v c1-w c1-x c1-y c1-z c1-10 c1-11 c1-12 c1-13 c1-b c1-c c1-14 c1-d c1-15 c1-16 c1-17 c1-e c1-f c1-g']").click()
time.sleep(5)

# step 1: open dropdown
driver.find_element(By.CSS_SELECTOR, "div.goog-te-gadget-simple").click()
time.sleep(1)

# step 2: wait for iframe and switch
iframe = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "iframe.goog-te-menu-frame"))
)
driver.switch_to.frame(iframe)

# step 3: JS click Spanish
spanish = driver.find_element(By.XPATH, "1")
driver.execute_script("arguments[0].click();", spanish)

driver.switch_to.default_content()
