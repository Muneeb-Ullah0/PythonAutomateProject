from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/register")

time.sleep(3)

# Fill in the registration details
driver.find_element(By.ID, "firstname").send_keys("Muneeb")
driver.find_element(By.ID, "lastname").send_keys("Khan")
driver.find_element(By.ID, "userName").send_keys("Muneebkhan922")
driver.find_element(By.ID, "password").send_keys("StrongPassword@123")

# CAPTCHA Handling (Manual Step)
print("Complete the CAPTCHA manually, then press Enter.")
input()

# Click the registration button
driver.find_element(By.ID, "register").click()
print("Registration button clicked successfully!")

# Wait for the response
time.sleep(3)

print("Registration submitted successfully!")

driver.quit()