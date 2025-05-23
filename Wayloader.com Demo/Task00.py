from tabnanny import check

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

print("Opening browser and navigating to page...")
driver.get("https://www.selenium.dev/documentation/webdriver/elements/locators/")

time.sleep(5)
print("Looking for 'Creating Locators' heading...")
element = driver.find_element(By.XPATH, "//h2[contains(text(),'Creating Locators')]")

print("Scrolling to element...")
driver.execute_script("arguments[0].scrollIntoView();", element)

print("Adding border for visual highlight...")
driver.execute_script("arguments[0].style.border='3px solid blue'", element)

time.sleep(5)
print("Test completed. Closing browser.")
driver.quit()

