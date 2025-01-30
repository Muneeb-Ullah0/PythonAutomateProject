from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the registration page
driver.get("https://demoqa.com/register")

# Wait for the page to load
time.sleep(3)

# Fill in the registration details
driver.find_element(By.ID, "firstname").send_keys("John")
driver.find_element(By.ID, "lastname").send_keys("Doe")
driver.find_element(By.ID, "userName").send_keys("JohnDoe123")
driver.find_element(By.ID, "password").send_keys("StrongPassword@123")

# CAPTCHA Handling (Manual Step)
print("Complete the CAPTCHA manually, then press Enter.")
input()

# Click the registration button
driver.find_element(By.ID, "register").click()
print("Registration button clicked successfully!")

# Wait for the response
time.sleep(3)

# Print Success Message
print("Registration submitted successfully!")

# Close the browser
driver.quit()