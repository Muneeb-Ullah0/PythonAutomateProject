from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://sixsigmatravels.com/")
time.sleep(2)

menu_links = [
    "Group Profile",
    "Company Profile",
    "Services",
    "Our Team",
    "Travel Ustaad",
    "Awards & Recognition",
    "Contact Us"
]

for link_text in menu_links:
    try:
        driver.find_element(By.LINK_TEXT, link_text).click()
        print(f"Opened: {link_text}")
        time.sleep(2)
    except Exception as e:
        print(f"Failed: {link_text} - {e}")
        break

driver.quit()
