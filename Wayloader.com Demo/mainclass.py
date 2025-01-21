from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome()

try:
    driver.get('https://12372.wayloader.com/login')


    time.sleep(10)

    username_field = driver.find_element(By.NAME, 'username')
    username_field.send_keys('womowi9591@acroins.com')

    password_field = driver.find_element(By.NAME, 'password')
    password_field.send_keys('Test@1234')

    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()

    time.sleep(5)
    print("Login successful!")

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()
