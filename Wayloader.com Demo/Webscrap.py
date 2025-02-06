import requests
from bs4 import BeautifulSoup

# URL to scrape
url = "https://example.com"  # Replace with the target website

# Send a GET request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
response = requests.get(url, headers=headers)

# Check if request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Example: Extract all <h1> tags
    headings = soup.find_all("h1")
    for h in headings:
        print(h.text.strip())

    # Example: Extract all links
    links = soup.find_all("a", href=True)
    for link in links:
        print(link["href"])
else:
    print(f"Failed to fetch page, status code: {response.status_code}")
