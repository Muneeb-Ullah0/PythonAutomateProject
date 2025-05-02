from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Credentials
email = "muneebnextgen@gmail.com"
password = "5cnKULTc"

# Setup
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.travelustaad.com/AAIST_B2B")

try:
    wait = WebDriverWait(driver, 15)

    # Wait for and fill email
    wait.until(EC.presence_of_element_located((By.ID, "Email User Name"))).send_keys(email)

    # Fill password
    driver.find_element(By.ID, "Password").send_keys(password)

    # Click login
    wait.until(EC.element_to_be_clickable((By.ID, "Login"))).click()

    # Wait for login success indicator (e.g., dashboard or user panel)
    wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Dashboard')]")))

    print("✅ Login successful!")

except Exception as e:
    print("❌ Login failed:", e)

finally:
    input("Press Enter to close browser...")
    driver.quit()
