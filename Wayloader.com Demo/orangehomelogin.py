from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

wait = WebDriverWait(driver, 15)

username = wait.until(EC.presence_of_element_located((By.NAME, "username")))
password = wait.until(EC.presence_of_element_located((By.NAME, "password")))

username.send_keys("Admin")
password.send_keys("admin123")

login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
login_button.click()

dashboard_text = wait.until(EC.presence_of_element_located((By.XPATH, "//h6[text()='Dashboard']")))

if dashboard_text:
    print("✅ Login successful! Navigated to Dashboard.")
    
else:
    print("❌ Login failed.")

print("Page Title after login:", driver.title)

driver.quit()
