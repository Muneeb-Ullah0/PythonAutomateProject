from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
    driver.get("https://www.google.com")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("python")
    search_box.send_keys(Keys.RETURN)

    search_button = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.NAME, "btnK"))
    )
    search_button.click()
except TimeoutException as e:
    print("Timeout occurred:", e)
except NoSuchElementException as e:
    print("Element not found:", e)
except Exception as e:
    print("An error occurred:", e)
finally:
    driver.quit()
