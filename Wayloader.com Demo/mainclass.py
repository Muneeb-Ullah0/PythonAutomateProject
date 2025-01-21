from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Optional: run Chrome in headless mode (no UI)

# Set up the webdriver using WebDriver Manager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Open a random website (you can replace this with any URL of your choice)
driver.get('https://www.example.com')

# Wait for the page to load
time.sleep(3)

# Example: Find a button and click on it
try:
    # Replace this XPath with the actual XPath of a button on the website you're automating
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//a[text()="More information..."]'))  # Update with the actual XPath
    )
    button.click()
    print("Button clicked!")
except Exception as e:
    print(f"Error occurred while clicking the button: {e}")

# Wait for a few seconds after the click action
time.sleep(3)

# If there are other actions to perform, you can add more code here. For example:
# Filling out a form:
try:
    # Example: Find an input field and fill it out (replace with actual field names or XPaths)
    input_field = driver.find_element(By.NAME, 'q')  # Example: search bar on a site
    input_field.send_keys('Selenium automation')
    input_field.submit()
    print("Form submitted!")
except Exception as e:
    print(f"Error occurred while submitting the form: {e}")

# Wait for the result page to load
time.sleep(3)

# Close the browser
driver.quit()
