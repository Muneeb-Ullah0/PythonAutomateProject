from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

wait = WebDriverWait(driver, 5)
driver.get("https://www.travelustaad.com/")

menu_links = [
    "Flight",
    "Groups",
    "Umrah",
    "Buses",
    "Hotels",
    "Holidays",
    "Visas"
]

for link_text in menu_links:
    try:
        link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, link_text)))
        driver.execute_script("arguments[0].click();", link)
        print(f"Opened: {link_text}")

        WebDriverWait(driver, 5).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
    except Exception as e:
        print(f"Failed to open {link_text}: {e}")
        continue

driver.quit()
