from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.google.com")

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("python")

search_box.send_keys(Keys.RETURN)

try:
    first_result = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.CSS_SELECTOR, "h3"))
    )
    
    first_result.click()
    
    # Take a screenshot and save it as screenshot.png
    driver.save_screenshot("screenshot.png")
    
    WebDriverWait(driver, 10).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )
except Exception as e:
    print("Error:", e)
finally:
    driver.quit()
