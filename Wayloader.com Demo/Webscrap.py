from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")  # Run in headless mode (no UI)
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920x1080")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# URL to scrape
url = "https://www.irishwheel.ie/user/create-ad"
driver.get(url)

# Get the page source after JavaScript loads
html_content = driver.page_source

# Save the HTML content
with open("scraped_page.html", "w", encoding="utf-8") as file:
    file.write(html_content)

# Close the driver
driver.quit()

print("HTML data successfully scraped and saved as 'scraped_page.html'.")
