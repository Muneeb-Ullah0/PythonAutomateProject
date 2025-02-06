from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Initialize WebDriver (No need to specify path manually)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open Google
driver.get("https://www.google.com")

# Find search box and enter query
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium Python")
search_box.send_keys(Keys.RETURN)

# Wait for results to load
time.sleep(2)

# Click on the first search result
first_result = driver.find_element(By.CSS_SELECTOR, "h3")
first_result.click()

# Wait and print page title
time.sleep(3)
print("Page Title:", driver.title)

# Close browser
driver.quit()
