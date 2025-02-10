from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# User Credentials
username = "womowi9591@acroins.com"
password = "Test@123"
login_url = "https://12372.wayloader.com/"

# Setup Chrome WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Initialize WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    # Open login page
    driver.get(login_url)

    # Wait for username & password fields
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='email']"))
    )
    password_field = driver.find_element(By.XPATH, "//input[@type='password']")

    # Enter credentials
    username_field.send_keys(username)
    password_field.send_keys(password)

    # Click the login button using provided class
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "login-button"))
    )
    login_button.click()

    # ✅ Verify successful login (Modify based on actual dashboard)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Dashboard')]"))  # Adjust if needed
    )

    print("✅ Login successful!")

except Exception as e:
    print("❌ Error:", e)

finally:
    # Keep browser open for testing
    input("Press Enter to close the browser...")
    driver.quit()
