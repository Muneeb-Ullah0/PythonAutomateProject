from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com")
search_box = driver.find_element_by_name("q")
search_box.send_keys("python")
print(driver.title)
driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Set up the Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the Google homepage
driver.get("https://www.google.com")

# Find the search box using the newer By.NAME method
search_box = driver.find_element(By.NAME, "q")

search_box.send_keys("python")
driver.implicitly_wait(10)  # Waits up to 10 seconds for elements

print(driver.title)

driver.quit()