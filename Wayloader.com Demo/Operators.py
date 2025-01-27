from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://mv-i.github.io/me/projects/login/dummy.html")

wait = WebDriverWait(driver, 10)
username_field = wait.until(EC.presence_of_element_located((By.ID, "username")))

username_field.send_keys("test_user")

password_field = wait.until(EC.presence_of_element_located((By.ID, "password")))

password_field.send_keys("test_password")
login_button = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
login_button.click()

import time
time.sleep(5)

driver.quit()
