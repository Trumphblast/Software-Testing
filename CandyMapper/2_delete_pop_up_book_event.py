'''
 When we open the website there is pop we try to remove it ,
  and create a Halloween event
'''

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

url = "https://candymapper.com/"

driver = webdriver.Edge()
driver.maximize_window()
driver.get(url)
time.sleep(5)

# Close popup
driver.find_element(By.ID, "popup-widget183-cta").click()
time.sleep(5)

# Click Book Event
driver.find_element(By.CSS_SELECTOR, ".x-el.x-el-a.c1-58.c1-59.c1-34.c1-18.c1-19.c1-5a.c1-s.c1-5e.c1-5f.c1-5g.c1-5h.c1-2d.c1-2b.c1-2a.c1-2c.c1-b.c1-4c.c1-1f.c1-27.c1-5b.c1-5c.c1-5d.c1-1g.c1-1h.c1-1i.c1-1j[aria-haspopup='false'][data-ux='NavLink'][data-page='820847bb-2740-4055-aa34-b49cdb177710']").click()

time.sleep(3)

# Click Book Now
driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > section:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1)").click()
time.sleep(3)

# Click Ghosts
driver.find_element(By.XPATH, "//a[normalize-space()='Ghosts']").click()
time.sleep(5)

# Switch to iframe if present (Wix booking form)
iframes = driver.find_elements(By.TAG_NAME, "iframe")
if len(iframes) > 0:
    driver.switch_to.frame(iframes[0])
    time.sleep(2)

# Select number of guests (using the correct ID "guests")
option_box = driver.find_element(By.ID, "guests")
select = Select(option_box)
select.select_by_visible_text("2")
time.sleep(2)

# Enter email
driver.find_element(By.CLASS_NAME, "x-el x-el-input c2-1 c2-2 c2-2o c2-2p c2-2l c2-2q c2-2r c2-2s c2-2t c2-2u c2-2v c2-2w c2-2x c2-2y c2-2z c2-3 c2-2f c2-4 c2-x c2-30 c2-31 c2-32 c2-33 c2-34 c2-35 c2-36 c2-37 c2-38 c2-39 c2-3a c2-2m c2-2n c2-5 c2-6 c2-7 c2-8").send_keys("bharath45@gmail.com")
time.sleep(3)

# Click submit button (use valid XPath for button)
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(3)

print("We created a Halloween event!")
driver.quit()
