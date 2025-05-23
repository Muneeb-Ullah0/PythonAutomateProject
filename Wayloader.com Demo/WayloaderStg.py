from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
username = "muneebnextgen@gmail.com"
password = "Test@1234"
login_url = "https://stg.wayloader.com/"
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    driver.get(login_url)

    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='email']"))
    )
    password_field = driver.find_element(By.XPATH, "//input[@type='password']")

    username_field.send_keys(username)
    password_field.send_keys(password)

    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "login-button"))
    )
    login_button.click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Dashboard')]"))
    )

    print("✅ Login successful!")

except Exception as e:
    print("❌ Error:", e)

finally:
    input("Press Enter to close the browser...")
    driver.quit()
