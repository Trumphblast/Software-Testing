'''
 here we log into Swag website , enter login details then  click login button
 and check out are we logined or not using Products string that appear when we  login
'''


from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.saucedemo.com/"
username = "standard_user"
password = "secret_sauce"

driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

driver.find_element(By.ID, "user-name").send_keys(username)
driver.find_element(By.ID, "password").send_keys(password)
driver.find_element(By.NAME, "login-button").click()


is_login_true = driver.find_element(By.CSS_SELECTOR,".title")
if is_login_true.text == "Products":
    print("Login Successful!")
else:
    print("Login Failed!")

driver.quit()